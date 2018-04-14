from django.shortcuts import render, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    if not "add" in request.session:
        request.session['add'] = ''
    return render(request,'words/index.html')

def form(request):
    print "test if"
    color = request.POST['color']
    word = request.POST['word']

    if "font" in request.POST:
        request.session['add'] += "<p class='"+color+" "+request.POST['font']+"'>"+word+"</p>"
    else:
        request.session['add'] += "<p class='"+color+"'>"+word+"</p>"
    return redirect('/')     

def logout(request):
    request.session.clear()
    return redirect('/')

