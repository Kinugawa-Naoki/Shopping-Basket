from django.urls import path
from ..views.views_stock import *

urlpatterns = [
    path('shopping_list/', shopping_listfunc, name='shopping_list'),
    path('add_shopping_list/', add_shopping_list_func, name='add_shopping_list'),
    path('create_shopping_list/', create_shopping_list_func, name='create_shopping_list'),
    path('how_to_user/', how_to_usefunc, name='how_to_use'),
]
