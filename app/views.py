from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def harish(request):
    return HttpResponse('something special')
def sunil(request):
    return HttpResponse('<marquee>IAM A DEVELOPER</marquee>')

