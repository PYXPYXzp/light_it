from django.conf.urls import url

from library.views import *

urlpatterns = [
    url(r'^author/$', AuthorList.as_view(), name='authors'),
    url(r'^book/(?P<pk>\d+)/$', BookDetail.as_view(), name='books_detail'),
    url(r'^add_book/$', AddBook.as_view(), name='add_book'),
    url(r'^add_author/$', AddAuthor.as_view(), name='add_author'),
    url(r'^$', FindBook.as_view(), name='books'),
    url(r'^author_books/$', AuthorBooks.as_view(), name='author_books'),
]
