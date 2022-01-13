from django.shortcuts import render
from rest_framework import viewsets
from .models import User,Salary
from .serializers import UserSerializer,SalarySerializer
from rest_framework.response import Response
from django.db.models import Avg



class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class SalaryView(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    

    def list(self,request,pk=None):
        lowest = 0
        biggest = 0
        average_salary = Salary.objects.all().aggregate(Avg('salary'))
        average_discount = Salary.objects.all().aggregate(Avg('discount'))    

        salary_query = Salary.objects.all().order_by('salary')

        if salary_query:
            lowest = salary_query.first().salary
            biggest = salary_query.last().salary


        salaries = []
        for salary in Salary.objects.all():
            salaries.append(SalarySerializer(salary).data)


        if(average_salary["salary__avg"]):
            average_salary_value =  round(average_salary["salary__avg"],2)
        else:
            average_salary_value = 0
        
        if(average_discount["discount__avg"]):
            average_discount_value = round(average_discount["discount__avg"],2)
        else:
            average_discount_value = 0
        data = {
            "lowest_salary":round(lowest,2),
            "biggest_salary":round(biggest,2),
            "average_salary":average_salary_value,
            "average_discount":average_discount_value,
            "salaries":salaries
            }
        return Response(data= data)
