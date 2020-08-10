#from django.db import models
from djongo import models

class Question(models.Model):
    question = models.CharField(max_length=200,null=True,blank=True)
    weighted = models.IntegerField()

    class Meta:
        abstract = True


class Answer (models.Model):

    answer = models.CharField(max_length=200)
    files = models.FileField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        abstract = True


class Claim(models.Model):
    _id = models.ObjectIdField()
    dni = models.CharField(max_length=10)
    email = models.EmailField()
    name = models.CharField(max_length=200)
    message = models.TextField(null=True,blank=True)
    files = models.FileField(upload_to='documents')
    priority = models.IntegerField(null=True,blank=True)
    state = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    questions = models.ArrayField( model_container = Question )
    answers = models.EmbeddedField( model_container = Answer )

    objects = models.DjongoManager()
   

    class Meta:
        verbose_name = 'Claim'
        verbose_name_plural = 'Claims'
    
class Request(models.Model):
    _id = models.ObjectIdField()
    dni = models.CharField(max_length=10)
    email = models.EmailField()
    name = models.CharField(max_length=200)
    plan = models.CharField(max_length=200)
    coin = models.CharField(max_length=200)
    state = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    objects = models.DjongoManager()
   

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'


class modelQuestions(Question):
    _id = models.ObjectIdField()

    class Meta(Question.Meta):
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class plan(models.Model):
    _id = models.ObjectIdField()
    tittle = models.CharField(max_length=50)
    price = models.IntegerField()
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)


    class Meta:
        verbose_name = 'plan'
        verbose_name_plural = 'planes'





