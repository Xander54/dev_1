from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Info
import pyqrcode
import png
import random
import os
import pytube

# Create your views here.
class Index(TemplateView):
    template_name='home.html'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        url=request.POST['url']
        save=Info(key=url)
        save.save()
        s=pyqrcode.create(url)
        num=random.randrange(2,221)
        cl=os.getcwd()
        os.chdir("C:/Users/moura/django-postgres/postgresTest/location_founder/static")
        s.png("img.png",scale=8)
        return render(request,'show.html',{"loc":cl})
    '''def post(self,request):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password_1=request.POST['password_1']
        note=''
        if password==password_1:
            user=User.objects.create_user(username,email,password)
            user.save(self)
        else:
            note='password not match!'

        return render(request,self.template_name,{'note':note})'''
class Other(TemplateView):
    template_name='other.html'
    def post(self,request):
        url=request.POST['url']
        yt=pytube.YouTube(url)
        yt.streams.first().download()

        return render(request,self.template_name)

        