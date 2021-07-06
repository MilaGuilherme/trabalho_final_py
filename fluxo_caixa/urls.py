from django.urls import path
from . import views

urlpatterns = [
    path('', views.fluxo, name='fluxo'),
    path('categorias', views.categorias, name='categorias'),
    path('categorias/delete/<int:id>', views.delete_categorias, name='delete_categorias'),
    path('contas/despesas', views.criar_a_pagar, name='criar_a_pagar'),
    path('contas/receitas', views.criar_a_receber, name='criar_a_receber'),
]