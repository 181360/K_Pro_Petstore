from django.urls import path

from .views import *

urlpatterns = [
    path('', product_list, name='product-list'),
    path('new/', product_new, name='product-new')
]