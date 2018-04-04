from django.conf.urls import url
from . import views
app_name='basicapp'
urlpatterns=[
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^schools/$',views.schoollistview.as_view(),name='schoolslist'),
    url(r'^schools/(?P<pk>[-\w]+)/$',views.schooldetailview.as_view(),name='schooldetail'),
    url(r'^create/$',views.schoolcreateview.as_view(),name='create'),
    url(r'^schools/update/(?P<pk>\d+)$',views.schoolupdateview.as_view(),name='update'),
    url(r'^schools/delete/(?P<pk>\d+)$',views.schooldeleteview.as_view(),name='delete'),
]
