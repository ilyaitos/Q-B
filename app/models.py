from django.db import models


class Person(models.Model):
    People = models.CharField(max_length=100)
    Salary = models.IntegerField()
    Prize = models.IntegerField()



