from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

#Create your models here.
class teaminfo(models.Model):
     team=models.OneToOneField(User,on_delete=models.CASCADE)

     member1=models.CharField(max_length=256)
     member2=models.CharField(max_length=256,blank=True)
     collegename=models.CharField(max_length=256)
     start_time = models.DateTimeField(default=datetime.now, blank=True)
     totalscore=models.PositiveIntegerField(default=0,blank=True)
     last_submit_time = models.DateTimeField(default=datetime.now, blank=True)
     total_time=models.DurationField(default=timedelta(0,0,0), blank=True)
     def __str__(self):
        return self.team.username

class question(models.Model):
     score = models.IntegerField()
     ans = models.CharField(max_length=256)
     question_name=models.CharField(max_length=256,blank=True)
     def __str__(self):
         if len(self.question_name)==0:
             return "Question"+str(self.pk)
         else:
             return self.question_name
