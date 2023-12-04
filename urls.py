from django.contrib import admin
from django.urls import path
from .views import (
    register,
    add_product,
    user_login,
    dashboard,
    show,
    manage_products,
    inner,
    index,
    registration_failed,
    add,
    payment_form,
    show_image,
    upload_image,
    imagedelete,
    cart,
    add_to_cart,
    book_product,
    remove_from_cart,
    remove_from_image,
    update_visibility,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register, name='register'),
    path('add_product/', add_product, name='add_product'),
    path('login/', user_login, name='login'),
    path('index/', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('show/', show, name='show'),
    path('manage_products/', manage_products, name='manage_products'),
    path('inner/', inner, name='inner'),
    path('registration_failed/', registration_failed, name='registration_failed'),
    path('add/', add, name='add'),
    path('payment_form/', payment_form, name='payment_form'),
    path('image/', show_image, name='image'),
    path('upload/', upload_image, name='upload'),
    path('imagedelete/<int:id>/', imagedelete, name='imagedelete'),
    path('update_visibility/<int:product_id>/', update_visibility, name='update_visibility'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:image_id>/', add_to_cart, name='add_to_cart'),
    path('book_product/<int:image_id>/', book_product, name='book_product'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('remove_from_image/<int:image_id>/', remove_from_image, name='remove_from_image'),
    path('add_to_cart/<int:image_id>/', add_to_cart, name='add_to_cart'),

]


