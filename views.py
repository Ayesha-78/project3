from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return httpResponse('<h1><marquee>this is ayesha</marquee></h1>')
