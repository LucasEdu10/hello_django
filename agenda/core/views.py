from django.shortcuts import render, redirect
from core.models import Evento

def index(request):
    
    return redirect('/agenda')

def lista_eventos(request):
    template = 'agenda.html'
    evento = Evento.objects.all()
    dados = {'evento': evento}
    
        
    return render(request,template, dados)


# Create your views here.
