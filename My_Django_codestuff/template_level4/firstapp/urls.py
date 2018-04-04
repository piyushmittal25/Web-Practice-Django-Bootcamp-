from django.conf.urls import url
from firstapp import views
app_name='firstapp'
urlpatterns=[
    url(r'^other/$',views.other,name='other'),
]
