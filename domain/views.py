from django.shortcuts import render, redirect
from domain.forms import UserForm, SignInForm, PaymentForm
from domain.models import UserProfile, UserPayments, UserExpense
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


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
                    return redirect("domain:sign_in")
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
            new_user = user_form.save()
            UserProfile.objects.create(user=new_user)
            # UserExpense.objects.create(user=new_user)
            messages.success(request, "Account created!")
            return redirect("domain:sign_in")
        else:
            for field, error_list in user_form.errors.items():
                for error in error_list:
                    messages.error(request, f"{field}: {error}")
                    return redirect("domain:user_registration")
    else:
        context = {
            "user_form": user_form,
        }
    return render(request, "registration/login.html", context)


@login_required(login_url="user_sign_in/")
def dashboard_view(request):
    """View to handle main dashboard view"""
    user_profile = UserProfile.objects.get(user=request.user)
    payments = UserPayments.objects.filter(user=request.user)
    expense = UserExpense.objects.filter(user=request.user)
    
    paginator = Paginator(payments, 5)
    page_num = request.GET.get("payment_table")
    page_obj = paginator.get_page(page_num)
    if request.method == "POST":
        print("POST")
        return render(request, "domain/dashboard/main.html", context)
    else:
        context = {
            "user_profile": user_profile,
            "payments": payments,
            "expenses": expense,
            "page_object": page_obj,
        }
    return render(request, "domain/dashboard/main.html", context)


def income_view(request):
    """View to handle income"""
    context = {
        'msg': "test",
    }
    return render(request, "domain/income/income.html", context)


def expense_view(request):
    """View to handle expense input"""
    context = {
        'msg': 'expense',
    }
    return render(request, "domain/expense/expense.html")


def payment_view(request, id):
    """View to handle payments"""
    payment_form = PaymentForm()
    context = {
        "payment_form": payment_form,
    }
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.user = request.user
            payment.save()
            
        return redirect("domain:home")
    
    return render(request, "domain/payment/payment.html", context)