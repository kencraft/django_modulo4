from django.urls import path

from .practica_api import  *
from .marvel_api_views import *

urlpatterns = [
    path('test/',test_api),
    path('test2/',test_api2),
    path('suma/',suma_post_api),
    path('get_comics/',get_comics),
    path('buy_comic/',purchased_item)
]
 