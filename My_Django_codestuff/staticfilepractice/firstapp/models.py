from django.db import models

# Create your models here.
class Topic(models.Model):
    Top_name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.Top_name
class Webpage(models.Model):
    topic=models.ForeignKey(Topic)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField(unique=True)
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage)
    date=models.DateField()
    def __str__(self):
        return str(self.date)
