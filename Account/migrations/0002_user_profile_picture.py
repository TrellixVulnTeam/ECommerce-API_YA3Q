# Generated by Django 3.2.4 on 2021-09-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='./staticfiles/user-avatar.png', upload_to='staticfiles'),
        ),
    ]
