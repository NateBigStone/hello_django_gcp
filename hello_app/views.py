from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Nathan Gaut - I.T. Visionary')
