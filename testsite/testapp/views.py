from django.shortcuts import render, HttpResponse
from django.views.generic import *
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    
    return render(request, 'testapp/index.html') 