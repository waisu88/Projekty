from django import forms 
from .models import Answer


class AnswerForm(forms.Form):

    answer_a = forms.BooleanField()    
    answer_b = forms.BooleanField() 
    answer_c = forms.BooleanField() 
         