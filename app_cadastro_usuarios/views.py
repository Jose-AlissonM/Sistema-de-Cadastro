from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save() #salvando os dados da tela para o BD

    #Exibir todos os usuarios ja cadastrados em um página
    exibir_usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # retornar os dados para a pagina de listagem de usuarios (usuarios.html)
    return render(request, 'usuarios/usuarios.html', exibir_usuarios)