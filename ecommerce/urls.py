from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecommerce, name='ecommerce'),
    path('item/<int:id>', views.item, name='item'),
    path('pagamento/', views.pagamento, name='pagamento')
]