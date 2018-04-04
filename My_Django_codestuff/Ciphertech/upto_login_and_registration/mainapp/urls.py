from django.conf.urls import url
from . import views

app_name='mainapp'

urlpatterns=[
    url(r'^$',views.InstructionView,name='instruction'),
    url(r'^leaderboard/$',views.LeaderboardView,name='leaderboard'),
    url(r'^teamlogin/$',views.LogInView,name='login'),
    url(r'^questionslist/$',views.QuestionListView,name='questionslist'),
]
