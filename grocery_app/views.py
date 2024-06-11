# grocery_app/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def blog(request):
    return render(request, 'blog.html')

def features(request):
    return render(request, 'features.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')

def error_404(request, exception):
    return render(request, '404.html', status=404)