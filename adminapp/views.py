from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import secrets
import string

def admin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(username)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
    return render(request,'adminlogin.html')

def dashboard(request):
    return render(request,'dashboard.html')

def add_department(request):
    if request.method == 'POST':
        dept_name=request.POST.get('dept_name')
        dept_desc=request.POST.get('dept_desc')
        dept=Department(dept_name=dept_name,dept_desc=dept_desc)
        dept.save()
    dep=Department.objects.all()
    return render(request,'add_department.html',{'dep':dep})

def edit_dept(request,pk):
    dept=Department.objects.get(id=pk)
    return render(request,'editdepartment.html',{'dept':dept})

def delete_dept(request,pk):
    dept=Department.objects.get(id=pk)
    dept.delete()
    return redirect('add_department')

def generate_password(length=6):
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def doctor(request):
    
    dept=Department.objects.all()
    doc=Doctor.objects.all()
    return render(request,'doctor.html',{'dept':dept,'doc':doc})


def adddoctor(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        username=request.POST.get('username')
        image = request.FILES.get('image')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        dept_id=request.POST.get('dept_name')
        dept_name=Department.objects.get(id=dept_id)
        password=generate_password()
        if image:
            doc=Doctor(name=name,image=image,mobile=mobile,address=address,department=dept_name,
                       username=username,password=password)
            doc.save()
        return redirect('doctor')
    
def edit_doc(request,pk):
    doc=Doctor.objects.get(id=pk)
    return render(request,'editdoctor.html',{'doc':doc})

def delete_doc(request,pk):
    dept=Doctor.objects.get(id=pk)
    dept.delete()
    return redirect('doctor')

def patient(request):
    pat=Patient.objects.all()
    return render(request,'patient.html',{'pat':pat})

def addpatient(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        username=request.POST.get('username')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        image = request.FILES.get('image')
        symptoms=request.POST.get('symptoms')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        password=generate_password()
        if image:
                doc=Patient(name=name,image=image,mobile=mobile,address=address,password=password,
                        username=username,symptoms=symptoms,gender=gender,dob=dob)
                doc.save()
        return redirect('patient')
    
def edit_patient(request,pk):
    pat=Patient.objects.get(id=pk)
    return render(request,'editpatient.html',{'pat':pat})

def delete_patient(request,pk):
    pat=Patient.objects.get(id=pk)
    pat.delete()
    return redirect('patient')

def appointment(request):
    return render(request,'appointment.html')

def doctor_records(request):
    return render(request,'doctor_records.html')

def register_doctor(request):
    return render(request,'register_doctor.html')

def approve_doctor(request):
    return render(request,'approve_doctor.html')

def doctor_specialization(request):
    return render(request,'doctor_specialization.html')

def patient_records(request):
    return render(request,'patient_records.html')

def admit_patient(request):
    return render(request,'admit_patient.html')

