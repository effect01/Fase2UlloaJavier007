from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, 'web/index.html')
    
def about(request):
    return render(request,'web/views/about.html')


def home(request):
    return render(request, 'web/views/home.html')



def contact(request): 
    return render(request,'web/views/contact.html')

def register(request):
    return render(request,'web/views/register.html')



def library(request):
    context = {
        'posts':Post.objects.all(),
      
    }
    return render(request, 'web/views/post.html', context)