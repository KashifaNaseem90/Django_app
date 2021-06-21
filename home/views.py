from django.shortcuts import render, HttpResponse
from django.http.response import HttpResponseBase
import csv

# Create your views here.
def landingpage(request):
    
    return render(request, 'landingpage.html')
    #return HttpResponse('Books')
def index(request):
    
    return render(request, 'index.html')

def listOfBooks(request):
   
    return render(request, 'book.html')

def cont(request):
   
  
    return HttpResponse('kashifanaseem90@gmail.com')
