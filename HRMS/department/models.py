from django.db import models
from employee.models import Employee

# Create your models here.
class Department(models.Model):
    department_name=models.CharField(max_length=50)
    department_code=models.CharField(max_length=10)


 #   class Manager(models.Model):
        #department_name=models.ForeignKey(Department,on_delete=True)
        #Manager_name=models.CharField(max_length=20)
        #manager_id=models.CharField(max_length=16)

class EmployeeDepartment(models.Model):
    department = models.ForeignKey(Department, related_name='department_employee', on_delete=models.CASCADE)
    employees = models.OneToManyField(Employee, related_name='employees')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department.department_name

class Attendance(models.Model):
    ABSENT="A"
    PRESENT="P"
    PERMISSION="PM"

    ATTENDANCE_STATUS=(
        (ABSENT,"Yasibye"),
        (PRESENT,"yatabiriye"),
        (PERMISSION,"Afite uruhushya")
    )
    department=models.ForeignKey(Department,related_name='attendances',on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee,related_name='employee_attendance',on_delete=models.CASCADE)
    attendance_status=models.CharField(choices=ATTENDANCE_STATUS,max_length=2,default=PERMISSION)  
    attended_on=models.DateField()    
    recorded_on=models.DateTimeField(auto_now_add=True)