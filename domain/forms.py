from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms import ModelForm, TextInput, PasswordInput, CheckboxInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError  
from domain.models import UserPayments, UserExpense

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2",]
        widgets = {
            "username": TextInput(attrs={"class": "form-control form-control-sm"}),
            "email": TextInput(attrs={"class": "form-control form-control-sm"}),
            "password1": PasswordInput(attrs={"class": "form-control form-control-sm"}),
            "password2": PasswordInput(attrs={"class": "form-control form-control-sm"}),
        }


class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password",]
        widgets = {
            "username": TextInput(attrs={"class": "form-control form-control-sm"}),
            "password": TextInput(attrs={"class": "form-control form-control-sm"}),
        }


class PaymentForm(ModelForm):
    class Meta:
        model = UserPayments
        exclude = ['date']
        fields = ['amount', 'description',]
        widgets = {
            "amount": TextInput(attrs={"class": "form-control form-control-sm"}),
            "description": TextInput(attrs={"class": "form-control form-control-sm"}),
        }


class ExpenseForm(ModelForm):
    class Meta: 
        model = UserExpense
        fields = ['paid', 'amount', 'description', 'payment_interval',]
        widgets = {
            "paid": CheckboxInput(attrs={"class": "form-check-input"}),
            "amount": TextInput(attrs={"class": "form-control form-control-sm"}),
            "description": TextInput(attrs={"class": "form-control form-control-sm"}),
            "payment_interval": TextInput(attrs={"class": "form-control form-control-sm"}),
        }