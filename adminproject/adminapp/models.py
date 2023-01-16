from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.IntegerField()
    marks = models.IntegerField()

    def __str__(self):
        return self.name