from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Course
# Create your views here.
def home(request):
    courses=Course.objects.all()

    return render(request,'home.html',context={'courses':courses})