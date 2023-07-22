from django.shortcuts import render

def test(request):
    context = {
        'msg': 'test',
    }
    return render(request, "domain/index.html", context)
