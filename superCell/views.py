from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests
clashofclans = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM3NTY4MTA4LWZiNmEtNGFmZi04ZDUxLTNmM2VkYjAwNjQ1MSIsImlhdCI6MTU2NDUxMzI1MSwic3ViIjoiZGV2ZWxvcGVyLzc5MjRkM2QxLTg0YTAtYzE1Yi05N2JiLTYyMWM4ZmMxNDVlMSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwOC4xNzAuOC4yNDIiXSwidHlwZSI6ImNsaWVudCJ9XX0.CiESSk6XK06-9KupyhWxBsANyFcaA2at3JiC5zjRFjOzODdHCyocpiPvTwYZ129zjc49tyXO_XYlxOXd8BZHSg"


def index(request):
    r = requests.get('https://api.clashofclans.com/v1/leagues')
    print(r)
    template = loader.get_template(
        'supercell/index.html')  # getting our template
    return HttpResponse(template.render(r))


def searchbyPlayer(request):
    template = loader.get_template(
        'supercell/index.html')  # getting our template
    return HttpResponse(template.render())


def searchbyClan(request):
    template = loader.get_template(
        'supercell/index.html')  # getting our template
    return HttpResponse(template.render())
