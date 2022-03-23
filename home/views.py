from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

def index(request):
    context = {
        "variable1": "This is Somya",
        "variable2": "How are you?"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def blogs(request):
    return render(request,'blogs.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name='name', email='email', phone='phone', desc='desc', date = datetime.today())
        contact.save()
        ##messages.success(request, 'You query has been sent')

    return render(request,'contact.html')
# Create your views here.
