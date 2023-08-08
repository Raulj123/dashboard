from django.shortcuts import render

def dashboard_view(request):
    context = {
        'msg': 'test',
    }
    return render(request, "domain/index.html", context)
