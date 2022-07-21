from django.urls import path

from . import views

urlpatterns = [
        path('produtos/', views.produtosLoja ),
        path('', views.listaProdutos, name='lista-produtos')
]
