from os import path

from django.core.paginator import Paginator

from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.all()
    }
    return render(request, template, context)

def one_book(request, date):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.filter(pub_date=date)
    }
    return render(request, template, context)

def bus_stations(request, date):

    paginator = Paginator(Book.objects.filter(pub_date=date), per_page=1)
    page_number = request.GET.get(date)
    print(page_number)
    page = paginator.get_page(page_number)
    # также передайте в контекст список станций на странице
    context = {
        'books': page,
        'page':  page_number

    }
    return render(request, 'books/books_list.html', context)


def ppp(request, date):
    lm = [i['pub_date'] for i in Book.objects.order_by('pub_date').values('pub_date')]
    paginator = Paginator(lm, per_page=1)
    page_number = date
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'books':  Book.objects.filter(pub_date=date)}
    return render(request, 'books/books_list.html', context)


