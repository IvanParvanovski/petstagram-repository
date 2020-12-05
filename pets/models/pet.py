from django.db import models

from account.models import UserProfile


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'

    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown')
    )

    type = models.CharField(max_length=7, choices=PET_TYPES, default=UNKNOWN, blank=False)
    name = models.CharField(max_length=6, blank=False,)
    age = models.PositiveIntegerField(blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images', blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'Id ({self.id}) --- ' \
               f'Name ({self.name}) --- ' \
               f'Type ({self.type}) ---' \
               f'Age ({self.age})'
