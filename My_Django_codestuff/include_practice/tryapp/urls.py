from django.urls import path
from tryapp import views
urlpatterns=[
    path('',views.index,name='index')
]
