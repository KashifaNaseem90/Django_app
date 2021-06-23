import csv
from django.http.response import HttpResponseBase

class HttpResponse(HttpResponseBase): 
    def __init__(self, name): 
        self.name = name 

lis = []
lis.append(( HttpResponse('The Alchemis-Paulo Coelho') ))
lis.append((HttpResponse('Eleven Minutes-Paulo Coelho')) )
lis.append((HttpResponse('The Zahir-Paulo Coelho')) )
books = []

for obj in lis:
    name = obj.name
    books.append(name)
with open('books.csv', 'w', newline='') as csv_1:
     csv_out = csv.writer(csv_1)
     csv_out.writerows([books[index]] for index in range(0, len(books)))

