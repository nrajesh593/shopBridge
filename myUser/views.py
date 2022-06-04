from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Login(request):
    html = "<html><body>Show Time</body></html>"
    return HttpResponse(html)
