# Generated by Django 4.0 on 2022-02-04 14:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport', '0007_remove_sportobject_follower'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportobject',
            name='follower',
            field=models.ManyToManyField(blank=True, null=True, related_name='objects', to=settings.AUTH_USER_MODEL),
        ),
    ]
