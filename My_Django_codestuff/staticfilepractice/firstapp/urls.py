from django.conf.urls import url
from firstapp import views
urlpatterns=[
    url(r'^',views.helpy,name='helpy'),
]
