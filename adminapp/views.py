from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
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

def doctor(request):
    return render(request,'doctor.html')

def patient(request):
    return render(request,'patient.html')

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

