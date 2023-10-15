from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    stock = models.IntigerField()
    def __str__(self):
        return self.name
    def check_stock(self):
        if self.stock > 0:
            return True
        else:
           return False





class Client(models.Model):
    name = models.CharField(max_length=235)
    lastname = models.CharField(max_length=255)
    email = models.emailField()
    phone = models.CharField(max_length=9)
    addr = models.CharField(max_length=210)
    def __str__(self):
       return self.name + " " + self.lastname 


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCASDE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntigerField()
    whole = models.DecimalField(max_digits=10, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.client) + " - " + str(self.product) + " - " + str(self.whole) + " - " + str(self.date_order)
