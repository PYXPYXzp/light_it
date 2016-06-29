from django.conf.urls import url, include

from library.views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^author/$', AuthorList.as_view(), name='authors'),
    url(r'^book/(?P<pk>\d+)/$', BookDetail.as_view(), name='books_detail'),
    url(r'^add_book/$', AddBook.as_view(), name='add_book'),
    url(r'^add_author/$', AddAuthor.as_view(), name='add_author'),
    url(r'^$', FindBook.as_view(), name='books'),
    url(r'^author_books/$', AuthorBooks.as_view(), name='author_books'),
    # url(r'^test/$', test_ang, name='test'),
    url(r'^library/$', api_authors, name='test'),
]

router = DefaultRouter()
router.register(r'authors', APIAuthorViewSet)
router.register(r'books', APIBookViewSet)

urlpatterns += [
    url(r'^api/', include(router.urls), name='api'),
]

# urlpatterns += [
#    url(r'^api-author-list/$', APIAuthorList.as_view(), name='APIauthorList'),
#     url(r'^api-book-list/$', APIBookList.as_view(), name='APIbookList'),
#     url(r'^api-book-detail/(?P<pk>[0-9]+)/$', APIBookDetail.as_view()),
# ]
