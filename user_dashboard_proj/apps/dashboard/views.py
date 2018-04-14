from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.

# login page
def index(request):
  return render(request, 'dashboard/index.html')

# main books page
# def success(request):
# #     if 'user_id' not in request.session:
# #         return redirect('/')
# #     else:
# #         context = {
# #             'user': User.objects.get(id=request.session['user_id']),
# #             'reviews': Review.objects.orderby('-created_at')[0:3],
# #             'books': Book.objects.all()
# #         }   
# #     return render(request, 'dashboard/books.html', context) 
def success(request):
    if 'id' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['id'])
        }
        return render(request, 'dashboard/books.html', context)  

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
    return redirect('/success')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    email = request.POST['email']
    request.session['id'] = User.objects.get(email=email).id
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')     

# books/add
def addBook(request):
    if 'id' not in request.session:
        return redirect('/')
    else: 
        context = {
            'authors': Author.objects.all()
        }   
        return render(request, 'dashboard/books_add.html') 
       

#post method for book creation
def createBook(request):
    if request.method == 'POST':
        if len(request.POST['author_name']) > 0:
            # creating new author
            author = Author.objects.create(name=request.POST['author_name'])
        else:
            # find author already in database
            author = Author.objects.get(id=request.POST['author_id'])   
        book = Book.objects.create(title=request.POST['title'], author=author)
        review = Review.objects.create(rating=request.POST['rating'], book=book, content=request.POST['content'], reviewer=User.objects.get(id=request.session['id']))
        return redirect('/books/{}'.format(book.id))
    return redirect('/books')     

#books/<id>
def showBook(request, id):
    if 'id' not in request.session:
        return redirect('/')
    else:
        context = {
            'book': Book.objects.get(id=id),
            'books': Book.objects.all()
        }    
    return render(request, 'dashboard/book.html', context)    

#post method for review creation
def addReview(request):
    if request.method == 'POST':
        book = Book.objects.get(id=request.POST['book_id'])
        reviewer = User.objects.get(id=request.session['id'])
        Review.objects.create(rating=request.POST['rating'], content=request.POST['content'], book=book, reviewer=reviewer)
        return redirect('/books/{}'.format(book.id))


#books/<id>/delete from books.html
def deleteReview(request, id): 
    review = Review.objects.get(id=id)
    book_id = review.book.id
    review.delete()
    return redirect('/books/{}'.format(book_id)) 

def userPage(request):
    if 'id' not in request.session:
        return redirect('/')   
    else:
        return render(request, 'dashboard/users.html') 

# def userPage(request, id):
#     if 'user_id' not in request.session:
#         return redirect('/')
#     else:
#         context = {
#             'user': User.objects.get(id=request.session['user_id']),
#             'email': User.objects.get(email = request.POST['email']),
#             'count': len(Review.objects.filter(id=request.session['user_id']))
#         }   
#     return render(request, 'dashboard/users.html', context) 