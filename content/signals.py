import os
from django.dispatch import receiver

from content.tasks import convert_480p
from .models import Video
from django.db.models.signals import post_save, post_delete
import django_rq


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print("Video wurde gespeichert")
    if created:
        print("Video wurde neu erstellt")
        queue = django_rq.get_queue("default", autocommit=True)
        print(instance.video_file.path)
        queue.enqueue(convert_480p, instance.video_file.path)
        # convert_480p(instance.video_file.path)


@receiver(post_delete, sender=Video)
def video_post_delete(sender, instance, *args, **kwargs):
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)
