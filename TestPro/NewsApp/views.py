from django import forms
from django.shortcuts import render ,redirect
from django.shortcuts import HttpResponse
from .models import News
from .forms import RegistrationForm
from .models import RegistrationData
# Create your views here.

def news(request):
    obj = News.objects.get(id=1)
    context = {
        "obj":obj
    }
    return render(request,'news.html' ,context) 


def news_date(request,year):
    article_list= News.objects.filter(pub_date__year = year)
    context ={'year':year, 'article_list':article_list}
    return render(request , 'newsdate.html',context)


def home(request):
    context={ "name":"Farooq","id":4567}
    return render(request,'home.html' ,context) 


def contact(request):
    return render(request,'contact.html')   


def register(request):
    context = {"form1":RegistrationForm}
    return render(request , 'signup.html' , context)

def add_user(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        myregister = RegistrationData(username = form.cleaned_data['username'],
                                    password = form.cleaned_data['password'],
                                    email = form.cleaned_data['email'],
                                    phone = form.cleaned_data['phone']) 

        myregister.save()  
    return redirect('home')                  
