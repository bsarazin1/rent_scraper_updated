
from django.db import models
from django.utils import timezone


class UserSearch(models.Model):
    user_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "User Search"


class Scrapy(models.Model):
    author = models.ForeignKey(
        UserSearch, on_delete=models.PROTECT, related_name='auth', blank=True, null=True)
    price = models.CharField(max_length=1000)  # current data
    location = models.TextField()
    beds = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    average = models.IntegerField(null=True, blank=True)
