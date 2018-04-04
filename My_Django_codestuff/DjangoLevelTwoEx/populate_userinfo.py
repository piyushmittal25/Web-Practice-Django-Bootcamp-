import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoLevelTwoEx.settings')

import django
django.setup()

###
from faker import Faker
fakegen=Faker()
from user.models import userinfo
def populate(n=5):
    for entry in range(n):
        fake_name=fakegen.name().split()
        fake_firstname=fake_name[0]
        fake_lastname=fake_name[1]
        fake_email=fakegen.email()
        userobject=userinfo.objects.get_or_create(First_name=fake_firstname,
                                                  Last_name=fake_lastname,
                                                  email=fake_email)[0]
        userobject.save()
if __name__=='__main__':
    print("start populating database...")
    populate(20)
    print("finished")
