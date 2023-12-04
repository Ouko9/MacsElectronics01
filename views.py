
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib import messages
from .forms import ProductForm, ImageForm
from .models import Member, Product, ImageModel, Cart, CartItem


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('homepage')
        else:
            return HttpResponseRedirect(reverse('registration_failed'))
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    return render(request, 'user_login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def manage_products(request):
    return render(request, 'manage_products.html')


def add(request):
    return render(request, 'add_products.html')


def inner(request):
    return render(request, 'inner-page.html')


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Member.objects.filter(username=username, password=password).exists():
            member = Member.objects.get(username=username, password=password)
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'user_login.html')
    else:
        return render(request, 'user_login.html')


def registration_failed(request):
    return render(request, 'registration_failed.html')


def payment_form(request):
    return render(request, 'payment_form.html')


def update_visibility(request, product_id):
    return render(request, 'update_visibility.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            title = form.cleaned_data['title']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']

            image_model = ImageModel.objects.create(title=title, price=price, image=image)

            return redirect('image')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Process the form data
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']

            product = Product.objects.create(name=name, price=price, description=description)

            return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'add_products.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/image')


def show(request):
    return render(request, 'show.html')


def book_product(request, image_id):
    # Retrieve the ImageModel instance or return a 404 response if not found
    image = get_object_or_404(ImageModel, id=image_id)

    return render(request, 'payment_form.html', {'image': image})


def add_to_cart(request, image_id):
    image = get_object_or_404(ImageModel, pk=image_id)

    # Check if the user has an existing cart
    if 'cart_id' in request.session:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(pk=cart_id)
    else:
        # Create a new cart if the user doesn't have one
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    # Create a new CartItem and associate it with the ImageModel
    CartItem.objects.create(
        cart=cart,
        product_name=image.title,
        product_price=image.price,
        product_image=image
    )
    return HttpResponseRedirect(reverse('add_to_cart', args=[image_id]))



def cart(request):
    # Retrieve the cart items associated with the current session
    cart_items = CartItem.objects.filter(cart__id=request.session.get('cart_id'))

    # Calculate the total price of items in the cart
    total_price = sum(item.product_price for item in cart_items)

    return render(request, 'add_to_cart.html', {'cart_items': cart_items, 'total_price': total_price})


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')


def remove_from_image(request, image_id):
    image = get_object_or_404(ImageModel, id=image_id)
    image.delete()
    return redirect('image')
