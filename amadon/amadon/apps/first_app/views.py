from django.shortcuts import render, redirect

def index(request):
    print "hi"
    return render(request, 'first_app/index.html')

def checkout(request):
    print "check out"
    prices = {
        "1012": 19.99,
        "1013": 4.99,
        "1014": 29.99,
        "1015": 49.99
    }
    request.session['quantity'] = request.POST['quantity']
    request.session['price'] = prices[request.POST['product_id']]
    request.session['total'] = float(request.session['quantity'])*float(request.session['price'])
    if 'sum' not in request.session:
        request.session['sum'] = 0
    else:
        request.session['sum'] += float(request.session['total'])
    if 'q' not in request.session:
        request.session['q'] = 0
    else:
        request.session['q'] += int(request.session['quantity'])            
    return redirect('/thanks')


def thanks(request):
    print "thanks"
    return render(request, 'first_app/checkout.html')
