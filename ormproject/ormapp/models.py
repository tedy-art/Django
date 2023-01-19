from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    E_id = models.IntegerField()
    salary = models.IntegerField()
    dept = models.CharField(max_length=100)

    def __str__(self):
        return self.name