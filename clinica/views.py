from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def agendamento(request):
    return render(request, 'agendamento.html')