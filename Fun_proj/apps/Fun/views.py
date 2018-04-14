from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
import bcrypt
from .models import *
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.

def index(request):
    return render(request, 'Fun/index.html')

def dashboard(request):
    if 'id' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['id']),
            'items': Wishlist.objects.filter(others=request.session['id']),
            'wishers': Wishlist.objects.filter(~Q(others=request.session['id']))
        }
        return render(request, 'Fun/dashboard.html', context)     

def loading(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    first_name = request.POST['fname'] 
    last_name = request.POST['lname']
    email = request.POST['email']
    password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
    request.session['id'] = user.id
    return redirect('/wish_items/dashboard')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    email = request.POST['email']
    request.session['id'] = User.objects.get(email=email).id
    return redirect('/wish_items/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')    

# add a new item button from dashboard, POST
def add_item(request):
    return render(request, 'Fun/add_item.html')   

# create a new item from add_item page, GET
def create(request):   
    if request.POST['product']:
        item = Wishlist.objects.create(name=request.POST['product'], user=User.objects.get(id=request.session['id']))
        this_item = Wishlist.objects.get(name=request.POST['product'])
        this_user = User.objects.get(id=request.session['id'])
        this_item.others.add(this_user)
    else:
        messages.error(request, 'Please enter a product') 
        return redirect('/wish_item/add_item')   
    return redirect('/wish_items/dashboard') 

def item(request, id):
    context = {
        'item': Wishlist.objects.get(id=id),
        'Users': User.objects.filter(wish_item=id)
    }
    return render(request, 'Fun/item.html', context)   

def delete(request, id):
    item = Wishlist.objects.get(id=id)   
    item.delete()
    return redirect('/wish_items/dashboard')

def remove(request ,id):
    if 'id' in request.session:
        this_item = Wishlist.objects.get(id=id)
        this_user = User.objects.get(id=request.session['id'])
        this_item.others.remove(this_user)
        return redirect('/wish_items/dashboard')  


def add(request, id): 
    if 'id' in request.session:
        this_item = Wishlist.objects.get(id=id)
        this_user = User.objects.get(id=request.session['id'])
        this_item.others.add(this_user)
        return redirect('/wish_items/dashboard')       
      


