from django.urls import include
from django.urls import path

urlpatterns = [
    path('', include('stocks.urls')),
    path('', include('orders.urls')),
]
