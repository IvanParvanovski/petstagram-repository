# Generated by Django 3.1.2 on 2020-11-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201128_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='/media/users/profile_pics/def_pic.png', upload_to='users/profile_pics/'),
        ),
    ]
