
from django.urls import path
from .views import Login

urlpatterns = [

    path('', Login, name="login"),

    # path('delete/<int:id>', Product_view.delete())
]
