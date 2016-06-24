# -*- coding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
import datetime
from library.models import *
from library.forms import *
from library.serializers import AuthorSerializer, BooksSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView


class Tabs(object):
    active_tab = None

    def get_context_data(self, **kwargs):
        context = super(Tabs, self).get_context_data()
        context['active'] = self.active_tab
        context['tabs'] = TabsMenu.objects.all()
        return context


class AuthorList(Tabs, ListView):
    model = Author
    template_name = 'library/author_list.html'
    active_tab = 'authors'


class BookDetail(Tabs, DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'


class AddBook(SuccessMessageMixin, Tabs, CreateView):
    model = Book
    # fields = ['title', 'author', 'user_now', 'user_before']
    template_name = 'library/book_create_form.html'
    success_url = reverse_lazy('library:books')
    form_class = AddBookForm
    active_tab = 'add_book'
    success_message = 'add book success!'


class AddAuthor(Tabs, CreateView):
    model = Author
    # fields = ['first_name', 'last_name']
    template_name = 'library/author_create_form.html'
    success_url = reverse_lazy('library:authors')
    form_class = AddAuthorForm
    active_tab = 'add_author'

    def get_context_data(self, **kwargs):
        context = super(AddAuthor, self).get_context_data()
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        if next_url:
            return next_url
        else:
            return reverse('library:books')


class FindBook(Tabs, ListView):
    model = Book
    template_name = 'library/book_list.html'
    active_tab = 'find_book'

    def get_context_data(self, **kwargs):
        context = super(FindBook, self).get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['search'] = self.request.GET.get('find')
        context['begin_date'] = self.request.GET.get('date1')
        context['end_date'] = self.request.GET.get('date2')
        try:
            context['sel_author'] = int(self.request.GET.get('select_author'))
        except (ValueError, TypeError):
            context['sel_author'] = ''
        return context

    def get_queryset(self):
        query = super(FindBook, self).get_queryset()
        title = self.request.GET.get('find')

        if title:
            query = query.filter(title__icontains=title)
        author = self.request.GET.get('select_author')
        if author:
            query = query.filter(author_id=author)
        begin_date = self.request.GET.get('start')
        end_date = self.request.GET.get('end')
        if self.validate_date(begin_date):
            query = query.filter(date__gte=begin_date)
        if self.validate_date(end_date):
            query = query.filter(date__lte=end_date)
        sort_query = self.request.GET.get('sorted')
        if sort_query:
            query = query.order_by(sort_query)
        return query

    @staticmethod
    def validate_date(date):
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except (TypeError, ValueError):
            return False
        return True


class AuthorBooks(Tabs, ListView):
    model = Book
    template_name = 'library/author_books_ajax.html'

    def get_queryset(self):
        query = super(AuthorBooks, self).get_queryset()
        author = self.request.GET.get('select_author')
        if author:
            query = Book.objects.filter(author=author)
        return query


class APIAuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class APIBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
