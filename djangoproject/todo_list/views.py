from django.http.response import HttpResponse
from django.shortcuts import render


def task(request):
    return HttpResponse('<h1>Hello Niggas</h1>')
# Create your views here.
