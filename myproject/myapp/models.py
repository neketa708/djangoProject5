from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

# Примеры функций CRUD для работы с моделями

def create_client(name, email, phone_number, address):
    new_client = Client(name=name, email=email, phone_number=phone_number, address=address)
    new_client.save()

def get_all_products():
    return Product.objects.all()

def update_client_address(client_id, new_address):
    client = Client.objects.get(id=client_id)
    client.address = new_address
    client.save()

def delete_order(order_id):
    order = Order.objects.get(id=order_id)
    order.delete()