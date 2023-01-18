from django.shortcuts import render
from employee.models import *
from employee.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class EmployeeAPI(APIView):
    def get(self, request):
        query = Employee.objects.all()
        serializer = EmployeeSerializer(query,many=True)
        return Response(serializer.data, status=200)

    def post(self,request):
        serializer= EmployeeSerializer(data=request.data,)
