from django.urls import path

app_name = 'recruiter_game'

from . import views

urlpatterns = [
    path('', views.recruiter_game, name='recruiter_game'),
]