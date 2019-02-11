from django.shortcuts import render
from .models import Job

def home(request):
    Jobs = Job.objects
    return render(request,'jobs/home.html',{'Jobs':Jobs})
# Create your views here.
