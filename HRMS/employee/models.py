from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name=models.CharField(max_length=20)
    employee_id=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.employee_name} - {self.employee_id}"
    