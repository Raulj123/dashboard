from django import forms
from domain.models import User
from django.forms import ModelForm, TextInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "occupation", "bio"]
        widgets = {
            "username": TextInput(attrs={"class": "form-control form-control-sm"}),
            "occupation": TextInput(attrs={"class": "form-control form-control-sm"}),
            "bio": TextInput(attrs={"class": "form-control form-control-sm"})

        }