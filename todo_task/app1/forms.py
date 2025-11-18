from django import forms

from app1.models import Todo
class AddTaskforms(forms.ModelForm):
    class Meta:
        model=Todo
        fields="__all__"