# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
# Inside your app's views.py file
from django.core.urlresolvers import reverse
from .models import Blog

# Example of an old index method:
def index(request):
    print("hello, I am your first request")
    return redirect('/target/this_app/new')
# Can be transformed to the following:
def index(request):
    print("hello, I am your first request")
    return redirect(reverse('my_new'))
    #In a views.py method
    # return redirect(reverse('users:new'))
    #In a views.py method
    # return redirect(reverse('users:show', kwargs={'id': your_id_variable }))




def update(request):
    errors = Blog.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/blog/edit/'+id)
        else:
            blog = Blog.objects.get(id = id)
            blog.name = request.POST['name']
            blog.desc = request.POST['desc']
            blog.save()
            return redirect('/blogs')

