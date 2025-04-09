
from django.contrib import admin
from django.urls import path
from app_cadastro_usuarios import views


urlpatterns = [
    # rota, view responsável, nome de referência         <-- estrutura padrão
    path('', views.home, name='home'),
    #aspas vazias indicam que a rota é a pagina inicial(home;inicio)
]
