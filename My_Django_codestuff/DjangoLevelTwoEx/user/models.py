from django.db import models

# Create your models here.
class userinfo(models.Model):
    First_name=models.CharField(max_length=250,unique=True)
    Last_name=models.CharField(max_length=250,unique=True)
    email= models.EmailField(max_length=250)
    def __str__(self):
        return self.First_name+" "+self.Last_name
