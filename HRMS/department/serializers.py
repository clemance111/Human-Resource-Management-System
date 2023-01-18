from rest_framework import serializers
from department.models import Department,Manager,Attendance,EmployeeDepartment


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields='__all__'

class EmployeeDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeDepartment
        fields='__all__' 

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'
    def validate(self, attrs):
        employee=attrs['employee']
        department=attrs['department']
        date=attrs['attended_on']
        if Attendance.objects.filter(employee=employee,department=department,attended_on=date).exists():
            raise serializers.ValidationError({"attendance_error":"we are done to record"})
        return super().validate(attrs)               