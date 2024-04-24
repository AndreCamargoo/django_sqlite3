from django.db import models


class Product(models.Model):
    name = models.CharField('name', max_length=100)
    price = models.DecimalField('price', decimal_places=2, max_digits=12)
    stock = models.IntegerField('stock')

    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    lastName = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.name} {self.lastName}'



