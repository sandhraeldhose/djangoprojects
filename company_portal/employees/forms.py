from django import forms

from employees.models import Employee
class Addviewforms(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
