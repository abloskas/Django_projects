from django.shortcuts import render, redirect 
from models import *
from django.contrib import messages 
# Create your views here.
def index(request):
    context = {
    'puppy': User.objects.all()
        }
    return render(request, 'users.html', context)

def user(request):
    return render(request, "users_new.html")    

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/user/new')    
    if request.method == "POST":
        User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'])
        return redirect('/users')

def show(request, id):
    return render(request, 'users_show.html', {'user': User.objects.get(id=id)})

def edit(request, id):
	return render(request, 'users_edit.html', {'user': User.objects.get(id=id)})    

def update(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/user/new')    
    else:
        user = User.objects.get(id = request.POST['id'])
        user.first_name = request.POST['fname']  
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()
        return redirect('/users') 
    
def remove(request, id):
    d = User.objects.get(id=id)  
    d.delete()
    return redirect('/users')  

