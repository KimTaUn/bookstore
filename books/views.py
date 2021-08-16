from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.files.storage import FileSystemStorage

from books.models import Book, Review

from books.form import ReviewForm

# import json

# booksData = open('D:/TUAN/Other/Python/web/bookstore/books/books.json')

# data = json.load(booksData)

# Create your views here.

# dbData = Book.objects.all()


class BookListView(ListView):
    # template_name = 'books/book_list.html'
    # context_object_name = 'books' => book_list in html template
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Book.objects.all()

# def index(request):

#     context = {'books': dbData}
#     return render(request, 'books/index.html', context )


class BookDetailView(DetailView):
    # login_url = '/login/'
    model = Book
    # template_name = "books/show.html"

    # overide get_context_data
    def get_context_data(self, **kwargs):
        # this is a book we have
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        context['form'] = ReviewForm
        return context


def review(request, id):
    if request.user.is_authenticated:
        # create a new review and save
        newReview = Review(
            book_id=id,
            user=request.user)
        # --- USE DJANGO FORM ---
        formset = ReviewForm(request.POST, request.FILES, instance=newReview)
        if formset.is_valid():
            formset.save()
        else:
            formset = ReviewForm()
            print('form is not valid')
        # ---- WAY 2 -----
        # body = request.POST['body']

        # # handle file upload
        # # fs = FileSystemStorage(location='media/images/review')
        # if len(request.FILES) != 0:
        #     image = request.FILES['image']
        #     fs = FileSystemStorage()
        #     name = fs.save(image.name, image)
        #     newReview.image = fs.url(name)
        # newReview.save()

    return redirect(f"/book/{id}")


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)


class AuthorDetailView(DetailView):
    pass

# def show(request, id):

#     # use try catch error
#     # try:
#     #     singleBook = Book.objects.get(pk = id)
#     # except Book.DoesNotExist:
#     #     raise Http404('Book does not found')

#     # use get_object_or_404
#     singleBook = get_object_or_404(Book, pk=id)
#     reviews = Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book': singleBook, 'reviews': reviews}
#     return render(request, 'books/show.html', context)


# def index(request):
    # # return HttpResponse('Hello books app')
    # context = {
    #     'name': 'tuan',
    #     'book' : {
    #         'title': 'The django',
    #         'thumbnailUrl': 'https://codelearn.io/CodeCamp/CodeCamp/Upload/Course/cf55489ccd434e8c81c61e6fffc9433f.jpg'
    #         }
    #     }
    # return render(request, 'books/index.html', context)
