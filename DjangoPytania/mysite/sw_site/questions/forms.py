from django import forms 
from .models import Answer

class AnswerForm(forms.Form):
    answer_a = forms.BooleanField(label="A",  )
    answer_b = forms.BooleanField()
    answer_c = forms.BooleanField()