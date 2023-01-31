from django.shortcuts import render

# Create your views here.ds
def index(response):
    return render(response, 'index.html', {})
    