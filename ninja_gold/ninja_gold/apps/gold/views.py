from django.shortcuts import render, redirect
from django.utils import timezone
import random

def index(request):
    if 'gold' in request.session:
        request.session['gold'] = request.session['gold']
    else:
        request.session['gold'] = 0    

    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []     
 

    request.session['farm'] = random.randrange(10, 21)
    request.session['cave'] = random.randrange(5, 11)
    request.session['house'] = random.randrange(2, 6)
    request.session['casino'] = random.randrange(-50, 51)
    request.session['temp'] = 0

    return render(request, 'gold/index.html')


def process(request):
    if request.POST['building'] == 'farm':
        request.session['gold'] += request.session['farm']
        request.session['temp'] = request.session['farm']
    if request.POST['building'] == 'cave':
        request.session['gold'] += request.session['cave']
        request.session['temp'] = request.session['cave']
    if request.POST['building'] == 'house':
        request.session['gold'] += request.session['house']
        request.session['temp'] = request.session['house']
    if request.POST['building'] == 'casino':
        request.session['gold'] += request.session['casino']     
        request.session['temp'] = request.session['casino'] 
 
    activity = ''
    if request.session['temp'] >= 0: 
        activity += 'Earned ' + str(request.session['temp']) + ' golds from the ' + str(request.POST['building'])
    if request.session['temp'] < 0:
        activity += 'Entered a casino and lost ' + str(request.session['temp']) + '...Ouch..'     

    # time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
    # activity += '! (' + str(time) + ')'
    request.session['activities'].insert(0, activity)
    
    return redirect(index)  
