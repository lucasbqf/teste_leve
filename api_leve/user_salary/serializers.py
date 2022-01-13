from rest_framework import serializers
from .models import Salary, User
from django.db.models import Avg

class UserSerializer(serializers.ModelSerializer):
    #fields gerados dinamicamente para cada usuario, é lido os salarios de cada usuario e 
    # realizado as medias e min max dos salarios para cada usuario
    biggest_salary = serializers.SerializerMethodField('get_biggest_salary')
    lowest_salary = serializers.SerializerMethodField('get_lowest_salary')
    average_salary = serializers.SerializerMethodField('get_average_salary')
    average_discount = serializers.SerializerMethodField('get_average_discount')

    def get_biggest_salary(self,user):
        biggest = Salary.objects.filter(user=user.id).order_by('-salary')
        if biggest:
            return round(biggest.first().salary,2)
        return 0

    def get_lowest_salary(self,user):
        lowest = Salary.objects.filter(user=user.id).order_by('salary')
        if lowest:
            return round(lowest.first().salary,2)
        return 0
    
    def get_average_salary(self,user):
        average = Salary.objects.filter(user=user.id).aggregate(Avg('salary'))
        if(average["salary__avg"]):
            return round(average["salary__avg"],2)
        return 0

    def get_average_discount(self,user):
        average = Salary.objects.filter(user=user.id).aggregate(Avg('discount'))
        if(average["discount__avg"]):
            return round(average["discount__avg"],2)
        return 0

    class Meta:
        model = User
        fields = ('cpf','name','bday','biggest_salary','lowest_salary','average_salary','average_discount')


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ('id','user','paydate','salary','discount')

