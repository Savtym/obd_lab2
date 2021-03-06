"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import mysql.connector
from .forms import ProductForm
from .db import Db
from django.shortcuts import redirect

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Manto',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Contacts of Manto',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Manto is shop for you',
            'year':datetime.now().year,
        }
    )

def products(request):
    """Renders the products page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/products.html',
        {
            'title':'Products',
            'message':'All products Manto',
            'year':datetime.now().year,
            'products':Db.getListProducts,
        }
    )

def product(request, id):
    """Renders the products page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/product.html',
        {
            'title':'Product',
            'message':'Product ' + id + ' of Manto',
            'year':datetime.now().year,
            'product':Db.getProduct(id),
        }
    )

def users(request):
    """Renders the products page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/users.html',
        {
            'title':'Users',
            'message':'All users Manto',
            'users' : Db.getListUsers(),
            'year':datetime.now().year,
        }
    )

def getProduct(request, id):
    """Renders the products page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/getProduct.html',
        {
            'title':'Product to add in cart',
            'message':'All users Manto',
            'users' : Db.getProductForUser(id, 2), # 2 - id user 
            'year':datetime.now().year,
        }
    )

def addProduct(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                name = form.data['name']
                title = form.data['title']
                categoryId = form.data['category']
                manufactoryId = form.data['manufactory']
                Db.addProduct(name, title, categoryId, manufactoryId)
                return redirect('/products')
        else:
            form = ProductForm()
        return render(
            request,
            'app/addProduct.html',
            {
                'title':'Add product',
                'message':'All users Manto',
                'year':datetime.now().year,
                'form' : form,
                'product' : "",
                'manufactories' : Db.getListManufactories,
                'categories' : Db.getListCategories,
            }
        )
    else:
      return redirect('/login') 

def editProduct(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                name = form.data['name']
                title = form.data['title']
                categoryId = form.data['category']
                manufactoryId = form.data['manufactory']
                Db.editProduct(id, name, title, categoryId, manufactoryId)
                return redirect('/product/' + id)
        else:
            product = Db.getProduct(id)
            form = ProductForm(initial={'name': product['name'], 'title' : product['title']})
        return render(
            request,
            'app/addProduct.html',
            {
                'title':'Edit product',
                'message':'All users Manto',
                'year':datetime.now().year,
                'form' : form,
                'product' : product,
                'manufactories' : Db.getListManufactories,
                'categories' : Db.getListCategories,
            }
        )
    else:
      return redirect('/login') 

def deleteProduct(request, id):
    if request.user.is_authenticated:
        product = Db.getProduct(id)
        return render(
            request,
            'app/removeProduct.html',
            {
                'title':'Remove product',
                'message':'All users Manto',
                'year':datetime.now().year,
                'msg' : Db.deleteProduct(id),
                'product' : product,
            }
        )
    else:
      return redirect('/login') 
