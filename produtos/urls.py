from django.urls import path

from . import views

urlpatterns = [
        path('', views.listaProdutos, name='lista-produtos')
]
