from django.db import models


# Create your models here.
class Card(models.Model):
    word = models.CharField(max_length=50, null=False, blank=False, default="")
    buzz_word_one = models.CharField(max_length=50, null=False, blank=False, default="")
    buzz_word_two = models.CharField(max_length=50, null=False, blank=False, default="")
    buzz_word_three = models.CharField(max_length=50, null=False, blank=False, default="")
    buzz_word_four = models.CharField(max_length=50, null=False, blank=False, default="")
    is_used = models.BooleanField(default=False)
