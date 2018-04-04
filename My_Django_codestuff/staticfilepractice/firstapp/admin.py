from django.contrib import admin
from firstapp.models import AccessRecord,Webpage,Topic
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
