from django.urls import path
from . import views 
urlpatterns =[
  path("products",views.product_list),
   path("",views.Api),
    path("products/<str:product>",views.product_detail)
]