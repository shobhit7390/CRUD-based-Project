from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','age','course']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'age':forms.TextInput(attrs={'class':'form-control'}),
                 'course':forms.TextInput(attrs={'class':'form-control'})}
