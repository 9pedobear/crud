from django import forms
from gridApp.models import *
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['name', 'contact', 'email']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact' : forms.TextInput(attrs={'class':'form-control'}),
        }
