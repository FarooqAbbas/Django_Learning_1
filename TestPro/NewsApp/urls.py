
from django.urls import path
from .views import news,contact,home,news_date,register ,add_user

urlpatterns = [

    path('', home,name='home'),
    path('news/', news,name='news'),   
    path('newsdate/<int:year>', news_date, name='newsdate'), 
    path('contact/', contact , name='contact'),
    path('signup/', register , name='register'),
     path('adduser/', add_user , name='adduser')
]