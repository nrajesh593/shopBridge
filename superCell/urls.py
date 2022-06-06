
from django.urls import path
from .views import index, searchbyClan, searchbyPlayer

urlpatterns = [
    path('', index, name='supercell index page'),
    path('searchplayer/', searchbyPlayer, name='searchplayer'),
    path('searchclan/', searchbyClan, name='searchclan'),

]
