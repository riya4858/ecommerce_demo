from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def departments(request):
    return render(request,'department.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    return render(request,'contact.html')