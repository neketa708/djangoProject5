from django.shortcuts import render
import logging
from datetime import datetime, timedelta
from .models import Client, Product, Order
# Create your views here.
# создаем логгер
logger = logging.getLogger('посещения')

# в представлениях
def главная(request):
    html = """<html>...</html>"""
    logger.info('Пользователь посетил страницу "главная"')

def о_себе(request):
    html = """<html>...</html>"""
    logger.info('Пользователь посетил страницу "о себе"')


# Create
def create_client(name, email, phone_number, address):
    new_client = Client(name=name, email=email, phone_number=phone_number, address=address)
    new_client.save()

def create_product(name, description, price, quantity):
    new_product = Product(name=name, description=description, price=price, quantity=quantity)
    new_product.save()

def create_order(client, products, total_amount):
    new_order = Order(client=client, total_amount=total_amount)
    new_order.save()
    new_order.products.add(*products)

# Read
def get_client_by_id(client_id):
    return Client.objects.get(id=client_id)

def get_product_by_id(product_id):
    return Product.objects.get(id=product_id)

def get_order_by_id(order_id):
    return Order.objects.get(id=order_id)

# Update
def update_client_address(client_id, new_address):
    client = Client.objects.get(id=client_id)
    client.address = new_address
    client.save()

def update_product_quantity(product_id, new_quantity):
    product = Product.objects.get(id=product_id)
    product.quantity = new_quantity
    product.save()

def update_order_total_amount(order_id, new_total_amount):
    order = Order.objects.get(id=order_id)
    order.total_amount = new_total_amount
    order.save()

# Delete
def delete_client(client_id):
    client = Client.objects.get(id=client_id)
    client.delete()

def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()

def delete_order(order_id):
    order = Order.objects.get(id=order_id)
    order.delete()


def order_list(request, client_id):
    client_orders = Order.objects.filter(client_id=client_id)
    current_date = datetime.now()
    ordered_products_last_7_days = get_ordered_products_in_period(client_orders, current_date - timedelta(days=7))
    ordered_products_last_30_days = get_ordered_products_in_period(client_orders, current_date - timedelta(days=30))
    ordered_products_last_365_days = get_ordered_products_in_period(client_orders, current_date - timedelta(days=365))

    return render(request, 'order_list.html', {
        'ordered_products_last_7_days': ordered_products_last_7_days,
        'ordered_products_last_30_days': ordered_products_last_30_days,
        'ordered_products_last_365_days': ordered_products_last_365_days,
    })


def get_ordered_products_in_period(client_orders, start_date):
    ordered_products = []
    for order in client_orders.filter(order_date__gte=start_date):
        for product in order.products.all():
            if product not in ordered_products:
                ordered_products.append(product)
    return ordered_products