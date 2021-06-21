import csv

from django.http.response import HttpResponseBase
class HttpResponse(HttpResponseBase): 
    def __init__(self, name, price): 
        self.name = name 
        self.price = price

lis = []
lis.append(( HttpResponse('The Alchemis-Paulo Coelho', '$0') ))
lis.append((HttpResponse('Eleven Minutes-Paulo Coelho', '$0' )) )
lis.append((HttpResponse('The Zahir-Paulo Coelho', '$0')) )
books = []
pricelist =[]

if __name__ == "__main__":
    for obj in lis:
        name = obj.name
        price = obj.price
        books.append(name)
        pricelist.append(price)
    with open('books.csv', 'w', newline='') as csv_1:
        csv_out = csv.writer(csv_1)
        csv_out.writerows([books[index]] for index in range(0, len(books)))

