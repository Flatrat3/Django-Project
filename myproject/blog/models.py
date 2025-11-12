from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Musician (models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name