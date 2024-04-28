from django.urls import path
from .views import order_list

urlpatterns = [
    path('client/<int:client_id>/orders/', order_list, name='order-list'),
    # другие пути
]