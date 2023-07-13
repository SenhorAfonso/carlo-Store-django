
from django.urls import path
from . import views

urlpatterns = [
    path('painel_admin/', views.painel_admin, name='painel_admin'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
]