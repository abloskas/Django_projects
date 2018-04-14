from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
#is root
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    print request.session['counter']
    return render(request,'random_word/index.html')

#/word from urls.py
def word(request):
    if request.method == 'POST':
        request.session['word'] = get_random_string(length=14)
        request.session['counter'] += 1
        return redirect('/')
    else:
        return redirect('/')

