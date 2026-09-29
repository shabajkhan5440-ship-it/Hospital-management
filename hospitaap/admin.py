from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = (

        "first_name",
        "last_name",

        "department",
        "status",
        "admission_date"
    )

    search_fields = (

        "first_name",
        "last_name",
        "mobile"
    )

    list_filter = (
        "status",
        "department",

    )

from django.contrib import admin

from .models import Lab_test, LabTest


@admin.register(Lab_test)
class Lab_testAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'age',
        'gender',
        'phone',
        'created_at'
    )

    search_fields = (
        'name',
        'phone',
        'email'
    )


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):

    list_display = (
        'test_name',
        'test_code',
        'category',
        'sample_type',
        'price',
        'status'
    )

    list_filter = (
        'category',
        'status'
    )

    search_fields = (
        'test_name',
        'test_code'
    )