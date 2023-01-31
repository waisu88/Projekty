from django.urls import path

app_name = 'questions'

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('practise/', views.practise, name='practise'),
    path('practise/<pk>/', views.single_question_view, name='single_question'),
    path('play/', views.PlayView.as_view(), name='play'),
]