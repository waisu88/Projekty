from django.shortcuts import render

# Create your views here.
def recruiter_game(response):
    return render(response, 'recruiter_game.html')