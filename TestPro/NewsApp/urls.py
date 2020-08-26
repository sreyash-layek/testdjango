

from django.urls import path
from .views import NewsP, Home, Contact, NewsDate

urlpatterns = [
    path('news/', NewsP, name="news"),
    path('', Home, name="home"),
    path('contact/', Contact, name="contact"),
    path('newsdate/<int:year>', NewsDate, name="newsdate")

]