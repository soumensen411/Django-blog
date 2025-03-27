from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,'base.html')
def home(request):
    return render(request,'index.html')
def menu(request):
    return render(request,'menu.html')
def order(request):
    return render(request,'order.html')
def about(request):
    return render(request,'about.html')
def feedback(request):
    return render(request,'feedback.html')