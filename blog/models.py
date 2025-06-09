from django.db import models


class Post(models.Model):
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # для удобства, выводим только первые 50 символов
