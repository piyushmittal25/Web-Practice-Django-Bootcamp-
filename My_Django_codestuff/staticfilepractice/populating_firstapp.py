import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','staticfilepractice.settings')



import django
django.setup()
## faker script
import random
import faker
from firstapp.models import  Topic,AccessRecord,Webpage

topic=['Torrent','Files','search','urli','python','java']
fakegen=faker.Faker()
def addTopic():
    top=Topic.objects.get_or_create(Top_name=random.choice(topic))[0]
    top.save()
    return top
def populate(n=5):
    for time in range(n):
        top=addTopic()
        ##craeting fake
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()
        ####
        webob=Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        acceob=AccessRecord.objects.get_or_create(name=webob,date=fake_date)[0]
if __name__=='__main__':
    print("Start populating")
    populate(20)
    print("Populating complete")
