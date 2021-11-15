from django.db import models
from django.contrib.auth.models import AbstractUser


def avatar_upload_path(instance, filename):
    return f"{instance.username}/{filename}"


class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to=avatar_upload_path, null=True, blank=True)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
