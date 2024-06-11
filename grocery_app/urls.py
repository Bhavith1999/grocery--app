# grocery_app/urls.py

from django.contrib import admin
from django.urls import path
from .views import home, about, product, blog, features, testimonial, contact, error_404


urlpatterns = [
    path('', home, name='home'),  # Root path
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('blog/', blog, name='blog'),
    path('features/', features, name='features'),
    path('testimonial/', testimonial, name='testimonial'),
    path('contact/', contact, name='contact'),
]

handler404 = 'grocery_app.views.error_404'
