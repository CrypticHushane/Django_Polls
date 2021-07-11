from django.urls import path
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path('polls', views.initial, name="home"),
    path('polls/about', views.about, name="about"),
    # ex: /polls/5/
    path('polls/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('polls/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]
