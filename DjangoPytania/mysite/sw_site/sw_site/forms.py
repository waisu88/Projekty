from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    is_recruiter = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_recruiter']


    #     user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField(blank=True)
    # recruiter = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)