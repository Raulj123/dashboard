from django.shortcuts import render
from domain.forms import UserForm
from domain.models import User
def dashboard_view(request):
    user_form = UserForm()
    users = User.objects.all()
    
    context = {
        "user_form": user_form,
        "users": users
    }

    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid() and user_form.has_changed():
            user_form.save()
        return render(request, "domain/dashboard/main.html", context)
    else:
        return render(request, "domain/dashboard/main.html", context)

def income_view(request):
    context = {
        'msg': "test",
    }
    return render(request, "domain/income/income.html", context)