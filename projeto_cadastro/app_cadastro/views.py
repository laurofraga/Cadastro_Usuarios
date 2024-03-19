from django.shortcuts import render
from .models import Usuario
def index (request):
    return render(request,"usuarios/index.html")

def usuarios (request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('Nome')
    novo_usuario.data_nasc = request.POST.get('date')
    novo_usuario.sexo = request.POST.get('Sex')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()
    
    usuarios = {
        'usuarios': Usuario.objects.all
    }    
    
    return render(request, 'usuarios/usuarios.html', usuarios)