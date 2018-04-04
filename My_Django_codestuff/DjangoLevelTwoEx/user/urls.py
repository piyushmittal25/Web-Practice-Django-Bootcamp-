from django.conf.urls import url
from user import views
urlpatterns=[
    url(r'^userinfo/$',views.users,name="user"),
    url(r'^newuser/$',views.newuser,name='newuser'),
    url(r'^newuser/thanksyou$',views.thankyou,name='thankyou'),
]
