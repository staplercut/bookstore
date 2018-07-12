from django.conf.urls import url
from . import views


app_name = 'logs'
urlpatterns = [
    url(r'^showlastten$', views.showlastten, name='showlastten'),
    url(r'^showbooklog$', views.showbooklog, name='showbooklog'),

]