from django import forms
from nicsapp.models import Product, ImageModel
from django.db import models

class MemberForm(forms.ModelForm):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.fullname} {self.username}"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

    # Add the following line to allow the form to be used without an associated model


class ImageForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    image = forms.ImageField()

    class Meta:
        model = ImageModel
        fields = ['title', 'price', 'image']



