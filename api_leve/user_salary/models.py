from django.db import models

class User(models.Model):
    cpf = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    bday = models.DateField()

    def __str__(self) -> str:
        return self.name

class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paydate = models.DateField()
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return self.salary