
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('realizar_login/', views.realizar_login, name='realizar_login'),
    path('realizar_cadastro/', views.realizar_cadastro, name='realizar_cadastro')
]

