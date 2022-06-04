
from django.urls import path
from .views import Product_view

urlpatterns = [

    path('', Product_view.as_view()),
    path('<int:id>', Product_view.as_view()),
    # path('delete/<int:id>', Product_view.delete())
]
