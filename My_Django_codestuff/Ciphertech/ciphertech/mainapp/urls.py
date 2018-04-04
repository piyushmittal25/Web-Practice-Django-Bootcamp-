from django.conf.urls import url
from . import views

app_name='mainapp'

urlpatterns=[
    url(r'^$',views.InstructionView,name='instruction'),
    url(r'^leaderboard/$',views.LeaderboardView,name='leaderboard'),
    url(r'^teamlogin/$',views.LogInView,name='login'),
    url(r'^questionslist/$',views.QuestionListView,name='questionslist'),
    url(r'^question1/$',views.Question1View,name="question1"),
    url(r'^question2/$',views.Question2View,name="question2"),
    url(r'^question3/$',views.Question3View,name="question3"),
    url(r'^question4/$',views.Question4View,name="question4"),
    url(r'^question5/$',views.Question5View,name="question5"),
    url(r'^question6/$',views.Question6View,name="question6"),
]
