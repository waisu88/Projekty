from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from .forms import UserForm, NewUserForm


def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="auth/register.html", context={"form":form})



def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    error_message = None
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect("/")
        else:
            error_message = "UPS, something went wrong"
    context = {
        "form": form,
        "error_message": error_message
    }        

    return render(request, "auth/login.html", context)



def index(request):
    return render(request, 'index.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

  
    def post(self, request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            
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