from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from department.serializers import *
from department.models import *
from employee.serializers import *
from employee.models import *

# Create your views here.
class DepartmentAPI(APIView):
    def get(self, request):
        query = Department.objects.all()
        serializer = DepartmentSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def update(self, request,):
        data = request.DATA
        qs = Department.objects.filter(Manager=2773951)
        serializer = DepartmentSerializer(qs, data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=203)

    def delete(self, request, format=None):
        department = Department.objects.filter(employee=2773951)
        department.delete()
        return Response(status=204)        

class  EmployeeDepartmentAPI(APIView):
    def get(self,request):
        query= EmployeeDepartment.objects.all()
        serializer = EmployeeDepartmentSerializer(query,many=True)
        return Response(serializer.data, status=200)
    
    def post(self,request):
        serializer = EmployeeDepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
    
    def update(self, request):
        data = request.DATA
        qs = EmployeeDepartment.objects.filter(Manager=2773951)
        serializer = EmployeeDepartmentSerializer(qs, data=data, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=203)
    
class AttendanceAPI(APIView):
    def get(self, request):
        query = Attendance.objects.all()
        serializer = AttendanceSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def update(self, request,):
        data = request.DATA
        qs = Attendance.objects.filter(Manager=2773951)
        serializer = AttendanceSerializer(qs, data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=203)

    def delete(self, request, format=None):
        department = AttendanceAPI.objects.filter(employee=2773951)
        department.delete()
        return Response(status=204)    
    