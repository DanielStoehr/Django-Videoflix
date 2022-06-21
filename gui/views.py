from django.shortcuts import render
from content.models import Video

# Create your views here.


def index(request):
    videos = Video.objects.all()
    return render(request, "gui/index.html", {"videos": videos})
