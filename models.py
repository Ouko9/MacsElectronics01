from django.db import models


# Create your models here.
class Member(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname


class ImageModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Add the 'price' field
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add the 'image' field
    description = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_items = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Add other fields as needed

    def __str__(self):
        return f"Cart {self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ForeignKey(ImageModel, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Add other fields as needed

    def save(self, *args, **kwargs):
        # Update subtotal before saving
        self.subtotal = self.quantity * self.product_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_name} in Cart {self.cart.id}"
