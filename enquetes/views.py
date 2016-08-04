from django.http import HttpResponse


def index(request):
    saudacao = "Bem vindo as enquetes!"
    return HttpResponse(saudacao)