from django.urls import path
from app_cadastro import views
urlpatterns = [
    path("", views.index, name="index"),
    path("usuarios/",views.usuarios, name="listagem_usuarios")
]
