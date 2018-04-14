from django.shortcuts import render, HttpResponse, redirect
def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
    print request.POST['name']
    print request.POST['desc']
    request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

