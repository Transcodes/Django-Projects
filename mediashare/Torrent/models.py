from django.db import models


class Torrent(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
