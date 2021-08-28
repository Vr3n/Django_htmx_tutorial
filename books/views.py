from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BookFormSet, BookForm
from .models import Author, Book

# Create your views here.

def create_book(request, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
        else:
            return render(request, "partials/book_form.html", context={
                "form": form
            })
    context = {
        "form": form,
        "author": author,
        "books": books
    }
    return render(request, "books/create_book.html", context=context)

def update_book(request, pk):
    books = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=books)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Updated Successfully") 
            return redirect("detail-book", pk=books.id)
        
    context = {
        "form": form,
        "book": books
    }
    return render(request, "partials/book_form.html", context=context)

def create_book_form(request):
    form = BookForm(request.POST or None)
    context = {
        "form": form
    }
    return render(request, "partials/book_form.html", context)

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        "book": book
    }
    return render(request, "partials/book_detail.html", context)
