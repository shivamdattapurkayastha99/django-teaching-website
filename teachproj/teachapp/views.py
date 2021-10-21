from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Course,Video
# Create your views here.
def home(request):
    courses=Course.objects.all()

    return render(request,'home.html',context={'courses':courses})
def coursepage(request,slug):
    
    course=Course.objects.get(slug=slug)
    # serial_number=request.GET.get('lecture')
    # video=Video.objects.get(course=course)
    print(course)
    context={'course':course}

    return render(request,'coursepage.html',context=context)