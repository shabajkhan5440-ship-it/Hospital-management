from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [

    path("dashboard/", views.dashboard, name="dashboard"),

    path(
        "add_patient/",
        views.add_patient,
        name="add_patient"
    ),

    path(
        "patients/",
        views.patient_list,
        name="patient_list"
    ),

     path(
        "Temprprory/",
        views.Temp,
        name="temprory"
    ),

    path(
        "Edit<int:id>/",
        views.edit_patient,
        name="patient_edit"
    ),
    path(
        "profile/",
        views.profile,
        name="profile"
    ),
    path(
        "Appointment/",
        views.Appointment,
        name="Appointment"
    ),
    path(
        "Doctor_list/",
        views.doctor_list,
        name="Doctor_list"
    ),
    path(
        "View/",
        views.Show_d,
        name="View"
    ),
    path
    ('Delete/<int:id>/', views.Delete, name='patient_delete'),

    path
    ('Doctor/<int:id>/', views.Doctor_d, name='doctor_delete'),

    path
    ('Billing/', views.create_bill, name='Billing'),
    path
    ('Bill_ditail/', views.Bill_ditail, name='Bill_ditail'),
    path('',views.Home,name='home'),
    path("help-center/",views.help_center,name="help_center"),


    path(
        'lab_test/',
        views.lab_tests,
        name='lab_tests'
    ),

    path(
        'Lab_patient/',
        views.Add_patient,
        name='Add_patient'
    ),

    path(
        'add_test/',
        views.add_lab_test,
        name='add_lab_test'
    ),

    path(
        'delete-test/<int:pk>/',
        views.delete_lab_test,
        name='delete_lab_test'
    ),

    path(
        'edit-test/<int:pk>/',
        views.edit_lab_test,
        name='edit_lab_test'
    ),

    path('demo/',views.Demo),
    path('About/',views.About),
    path('Contact/',views.Contact),
    path('Service/',views.Service),
    path("labratory/",views.Labratory),
    path("labratory_doctor/",views.Labratory_doctor),
    path('labratory_addpatentie/',views.Labratory_addpatente)
]


