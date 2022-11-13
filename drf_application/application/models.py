from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Dictionary(models.Model):
    label=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    search_count=models.CharField(max_length=10)
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.label