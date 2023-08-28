from django.shortcuts import render, redirect
from domain.forms import UserForm, SignInForm
from domain.models import UserProfile
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def logout_view(request):
    """View to handle loging out"""

    if request.method == "POST":
        logout(request)
    return render(request, "registration/signin.html")


def sign_in(request):
    """View to handle signing and handling errors"""

    signin_form = SignInForm()

    if request.method == "POST":
        signin_form = SignInForm(data=request.POST)

        if signin_form.is_valid():
            user = signin_form.get_user()
            login(request, user)
            return redirect("domain:home")
        else:
            for field, error_list in signin_form.errors.items():
                for error in error_list:
                    messages.error(request, f"{field}: {error}")
    else:
        context = {
            "signin_form": signin_form,
        }
    return render(request, "registration/signin.html", context)


def user_registration(request):
    """View to handle registration and handle errors"""

    user_form = UserForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Account created!")
            return redirect("domain:sign_in")
        else:
            for field, error_list in user_form.errors.items():
                for error in error_list:
                    messages.error(request, f"{field}: {error}")
    else:
        context = {
            "user_form": user_form,
        }
    return render(request, "registration/login.html", context)


@login_required(login_url="user_sign_in/")
def dashboard_view(request):
    """View to handle main dashboard view"""
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        print("POST")
        return render(request, "domain/dashboard/main.html", context)
    else:
        context = {
            "user_profile": user_profile,
        }
    return render(request, "domain/dashboard/main.html", context)


def income_view(request):
    """View to handle income"""
    context = {
        'msg': "test",
    }
    return render(request, "domain/income/income.html", context)
