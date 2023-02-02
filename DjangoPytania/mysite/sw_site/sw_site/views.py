from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm





def index(response):
    # context = {
    #     'proba': "nic tu nie wyśiwetla"
    # }
    return render(response, 'index.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            is_recruiter = form.cleaned_data['is_recruiter']
            user.set_password(password)
            user.save()


            user = authenticate(username=username, password=password)
            print(user)
            print(user.username)
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect("/")

                    
        return render(request, self.template_name, {'form': form})