from django.shortcuts import render
from django.http import HttpResponse
from .models import Add
# Create your views here.
def index(request):
    employees=Add.objects.all
    # return HttpResponse("<h1>ABC</h1>")
    return render(request,'index.html',{'employees': employees})
def About(request):
    return HttpResponse("<h1>About</h1>")
def contact(request):
    return HttpResponse("<h1>Contact</h1>")
