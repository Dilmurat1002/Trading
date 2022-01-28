from django.db import models

# Create your models here.


class Firms(models.Model):
    name = models.CharField('Название', max_length=100)
    first_name = models.CharField('Имя руководителя', max_length=100)
    second_name = models.CharField('Фамилия руководителя', max_length=100)
    third_name = models.CharField('Отчество руководителя', max_length=100)
    addres = models.CharField('Адрес', max_length=100)

class Products(models.Model):
    name = models.CharField('Название', max_length=100)
    price = models.IntegerField('Цена', max_length=50)
    unit = models.CharField('Единица измерения', max_length=50)

class Sales(models.Model):
    name = models.CharField('Название', max_length=100)
    payment_account = models.IntegerField('Рассчетный счет', max_length=100)
    number = models.IntegerField('Количество', max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    firm = models.ForeignKey(Firms, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)






