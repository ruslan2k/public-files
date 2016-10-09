from django.db import models
from django.contrib.auth.models import Group

#from my

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class SecurityGroup(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    custom_field = models.CharField(max_length=191)
