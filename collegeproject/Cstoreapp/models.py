from django.db import models
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    objects = None
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def __str__(self):
        return '{}'.format(self.name)
class Courses(models.Model):
    objects = None
    cname=models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    class Meta:
        ordering=('cname',)
        verbose_name='course'
        verbose_name_plural='courses'


    def __str__(self):
        return '{}'.format(self.cname)

class Product(models.Model):
    objects = None
    pname=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)

    class Meta:
        ordering=('pname',)
        verbose_name='product'
        verbose_name_plural='productss'



    def __str__(self):
        return '{}'.format(self.pname)

class Register:
    pass

