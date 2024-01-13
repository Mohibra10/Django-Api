from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response 

@api_view(["GET"])
def Api(request):
  api=[
  "products/","products/:name"
  ]
  return Response (api)

@api_view(["GET","POST"])  
def product_list (request):
  products=["iphone", "Television", "Washing machine"]
  
  return Response (products)
  #return HttpResponse (items)
  
  
def product_detail(request, product):
  data=product
  
  return JsonResponse (product, safe=False)