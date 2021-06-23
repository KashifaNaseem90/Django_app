from django.shortcuts import render, HttpResponse
from django.http.response import HttpResponseBase
import csv

def landingpage(request):
    
    return render(request, 'landingpage.html')
    #return HttpResponse('Books')
def index(request):
    
    return render(request, 'index.html')

def listOfBooks(request):
    lis = []
    lis.append(('The Alchemis-Paulo Coelho') )
    lis.append(('Eleven Minutes-Paulo Coelho')) 
    lis.append(('The Zahir-Paulo Coelho')) 
    return render(request, 'book.html', {'result':lis})

def cont(request):
  
    return HttpResponse('kashifanaseem90@gmail.com')
