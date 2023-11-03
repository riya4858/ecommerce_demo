from django.urls import path
from .import views
urlpatterns = [
    path('admin',views.admin,name='admin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('doctor',views.doctor,name='doctor'),
    path('patient',views.patient,name='patient'),
    path('appointment',views.appointment,name='appointment'),
    path('doctor_records',views.doctor_records,name='doctor_records'),
    path('register_doctor',views.register_doctor,name='register_doctor'),
    path('approve_doctor',views.approve_doctor,name='approve_doctor'),
    path('doctor_specialization',views.doctor_specialization,name='doctor_specialization'),
    path('patient_records',views.patient_records,name='patient_records'),
    path('admit_patient',views.admit_patient,name='admit_patient'),
]