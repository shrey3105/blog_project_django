from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=264)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.question

class Options(models.Model):
    option=models.CharField(max_length=50)
    votes=models.IntegerField(default=0)
    question=models.ForeignKey(Question,max_length=264,on_delete=models.CASCADE,related_name='questions')

    def __str__(self):
        return self.option
