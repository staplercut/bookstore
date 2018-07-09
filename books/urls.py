from django.conf.urls import url
from .views import (
    book_detail,
    book_new,
    book_edit,
    book_delete,
    book_manage,
)

app_name = 'books'
urlpatterns = [
    url(r'^book/(?P<pk>\d+)/$', book_detail, name='book_detail'),
    url(r'^book/new/$', book_new, name='book_new'),
    url(r'^book/(?P<pk>\d+)/edit/', book_edit, name='book_edit'),
    url(r'^book/(?P<pk>\d+)/delete', book_delete, name='book_delete'),
    url(r'^manage/', book_manage, name='book_manage')
]
