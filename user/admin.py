from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        ("Individuelle Daten", {"fields": ("custom", "phone", "address")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
