from django.shortcuts import render, redirect


def index(request):
    return render(request, "survey/index.html")


def main(request):
    print "hello"
    if not "submit" in request.session:
        request.session['submit'] = 1
    else: 
        request.session['submit'] += 1
    print "you're welcome"

    request.session["fullname"] = request.POST['full_name']
    request.session["locations"] = request.POST['locations']
    request.session["languages"] = request.POST['languages']
    request.session["commentform"] = request.POST['comment-form']
    return redirect("/survey/result")


def results(request):
    return render(request, "survey/results.html")
