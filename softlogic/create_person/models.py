from django.db import models
from django_mysql.models import JSONField

# Create your models here.


class Person(models.Model):

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"

    def __str__(self):
        return self.second_name + ' ' + self.first_name[0] + '.'

    first_name = models.CharField(verbose_name="Имя", max_length=64)
    second_name = models.CharField(verbose_name="Фамилия", max_length=128)
    vector = JSONField(verbose_name="Векторное представление", blank=True)
