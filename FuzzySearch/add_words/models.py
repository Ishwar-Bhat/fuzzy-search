from django.db import models


class WordsList(models.Model):
    word = models.CharField(primary_key=True, max_length=100, blank=False)
    frequency = models.IntegerField(null=False)
