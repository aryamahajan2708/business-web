from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joining_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Person(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length= 200)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
    email = models.EmailField()


    def __str__(self):
        return f"{self.firstName} {self.lastName}"
