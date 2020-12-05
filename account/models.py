from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default='/media/users/profile_pics/def_pic.png',
        upload_to='users/profile_pics/',
        blank=True,
    )

    def __str__(self):
        return self.user.username
