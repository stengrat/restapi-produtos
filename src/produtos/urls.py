from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.ProductList.as_view()),
    path('estabelecimentos/',views.EstablishmentList.as_view()),
]