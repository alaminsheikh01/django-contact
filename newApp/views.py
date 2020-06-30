from django.shortcuts import render , HttpResponse
from newApp.models import Contact
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        about = Contact(name=name,email=email,desc=desc,date= datetime.today())
        about.save()
    return render(request, 'about.html')


def service(request):
    return render(request,'service.html')

def blog(request):
    return render(request,'blog.html')