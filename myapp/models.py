from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=250, primary_key=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name