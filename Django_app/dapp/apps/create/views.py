from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = 'placeholder to later display all the list of blogs'
    return HttpResponse(response)

def create(request):
    response = 'creatttting'
    return redirect('/')

def new(request):
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)    

def show(request, number):
    response = 'placeholder to display blog' +str(number)
    return HttpResponse(response)

def edit(request, number):
    response = 'placeholder to edit blog' +str(number)   
    return HttpResponse(response)


def destroy(response, number):
    response = 'placeholder to edit blog' +str(number) 
    return redirect('/')