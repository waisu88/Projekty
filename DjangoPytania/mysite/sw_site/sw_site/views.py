from django.shortcuts import render

def index(response):
    # context = {
    #     'proba': "nic tu nie wyśiwetla"
    # }
    return render(response, 'index.html')