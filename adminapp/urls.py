from django.urls import path
from .import views
urlpatterns = [
    path('admin',views.admin,name='admin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('add_department',views.add_department,name='add_department'),
    path('edit_dept/<int:pk>/',views.edit_dept,name='edit_dept'),
    path('delete_dept/<int:pk>',views.delete_dept,name='delete_dept'),
    path('doctor',views.doctor,name='doctor'),
    path('adddoctor',views.adddoctor,name='adddoctor'),
    path('edit_doc/<int:pk>/',views.edit_doc,name='edit_doc'),
    path('delete_doc/<int:pk>',views.delete_doc,name='delete_doc'),
    path('patient',views.patient,name='patient'),
    path('addpatient',views.addpatient,name='addpatient'),
    path('edit_patient/<int:pk>',views.edit_patient,name='edit_patient'),
    path('delete_patient/<int:pk>',views.delete_patient,name='delete_patient'),
    path('appointment',views.appointment,name='appointment'),
    path('doctor_records',views.doctor_records,name='doctor_records'),
    path('register_doctor',views.register_doctor,name='register_doctor'),
    path('approve_doctor',views.approve_doctor,name='approve_doctor'),
    path('doctor_specialization',views.doctor_specialization,name='doctor_specialization'),
    path('patient_records',views.patient_records,name='patient_records'),
    path('admit_patient',views.admit_patient,name='admit_patient'),
]