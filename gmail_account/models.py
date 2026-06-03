from django.db import models

class Gmail(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gmail = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.username