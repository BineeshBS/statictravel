from django.db import models


# Create your models here.
# Creating table for model.

class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField('Pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField('images')
    desc = models.TextField()

    def __str__(self):
        return self.name
