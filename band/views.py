from django.shortcuts import render

# Create your views here.


def index(request):
    r = "x"
    return render(request, 'band/index.html', {'data': r})
