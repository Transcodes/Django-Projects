from django.db import models
import datetime

class Link(models.Model):
    title = models.CharField(max_length=200, default="")
    date = models.DateTimeField('date')
    tag = models.CharField(max_length=50, default="")
    link = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    size = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.title
        return self.tag

