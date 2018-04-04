from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=254)
    location=models.CharField(max_length=254)
    principal=models.CharField(max_length=254)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("basicapp:schooldetail",kwargs={'pk':self.pk})

class Student(models.Model):
    name=models.CharField(max_length=254)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(School,related_name='students')
    def __str__(self):
        return self.name
