
from django.urls import path
from .views import User_view

urlpatterns = [

    path('', User_view.as_view()),
    path('<int:id>', User_view.as_view()),
    # path('delete/<int:id>', Product_view.delete())
]
