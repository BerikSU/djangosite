from django.shortcuts import render, get_object_or_404
from .models import Category, Product
import datetime

def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
  
    time = datetime.datetime.now()
    hour = time.hour
    minute = time.minute
    second = time.second
    year = time.year
    month = time.month
    day = time.day
    w_day = time.weekday()
    
    
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,'num_visits':num_visits,'hour': hour, 'minute': minute, 'second': second, 'year': year,
        'month': month, 'day': day, 'weekday': w_day,
    })

def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product}) 