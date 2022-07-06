import datetime

from django.db import models
from django.utils import timezone
class Question(models.Model):
    #id
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published",auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id) +': '+ self.question_text +': '+ str(self.pub_date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.datetime.now()

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)#se elimina una question se van a eliminar todos los choices
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return str(self.id) +': '+ self.choice_text
