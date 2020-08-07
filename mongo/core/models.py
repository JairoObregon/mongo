#from django.db import models
from djongo import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=200,null=True,blank=True)
    weighted = models.IntegerField()

    class Meta:
        abstract = True



class Claim(models.Model):
    _id = models.ObjectIdField()
    dni = models.CharField(max_length=10)
    email = models.EmailField()
    name = models.CharField(max_length=200)
    message = models.TextField(null=True,blank=True)
    files = models.FileField(null=True,blank=True)
    priority = models.IntegerField(null=True,blank=True)
    state = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    questions = models.ArrayField( model_container = Question    )
    objects = models.DjongoManager()
   

    class Meta:
        verbose_name = 'Claim'
        verbose_name_plural = 'Claims'

class Answer (models.Model):
    _id = models.ObjectIdField()
    answer = models.CharField(max_length=200,null=True,blank=True)
    files = models.FileField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    claim = models.EmbeddedField( model_container = Claim ,  blank=False)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


