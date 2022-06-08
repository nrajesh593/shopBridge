from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests
clashofclans = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImFiNGU2ODIwLWU4NjEtNGRlZi04ZGVkLWMwMDBjN2FhNjNjYSIsImlhdCI6MTY1NDUyNDU3MCwic3ViIjoiZGV2ZWxvcGVyLzc5MjRkM2QxLTg0YTAtYzE1Yi05N2JiLTYyMWM4ZmMxNDVlMSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE3NS4xMDEuMTcuMjI5Il0sInR5cGUiOiJjbGllbnQifV19.nnO0luLcXm6CwKtBdlxIsd4Yq0bPYzbe4U1XAhFTtwiP0Y2llHe7aPGaW8AhbgLST-JoTwqYdedI6rlmiPXGMA"


def index(request):
    r = requests.get('https://api.clashofclans.com/v1/leagues',
                     headers={'Authorization': "Bearer "+clashofclans})
    # t = template.loader.get_template('supercell/index.html')
    # c = template.Context({"data": r})
    # html = t.render(c)
    # return HttpResponse(html)
    return render(request, 'supercell/index.html', {'data': r})


def searchbyPlayer(request):
    template = loader.get_template(
        'supercell/index.html')  # getting our template
    return HttpResponse(template.render())


def searchbyClan(request):
    template = loader.get_template(
        'supercell/index.html')  # getting our template
    return HttpResponse(template.render())
