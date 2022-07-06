from django.db import models

class Question(models.Model):
    #id
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choices(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)#se elimina una question se van a eliminar todos los choices
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
