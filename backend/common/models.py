from django.db import models


class TimeStampedModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True
