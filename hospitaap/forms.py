from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        exclude = ["patient_id", "created_at"]

        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
            "admission_date": forms.DateInput(attrs={"type": "date"}),
            "discharge_date": forms.DateInput(attrs={"type": "date"}),
            "address": forms.Textarea(attrs={"rows":3}),
            "disease": forms.Textarea(attrs={"rows":3}),
        }

from django import forms
from .models import Lab_test, LabTest


class Lab_testForm(forms.ModelForm):

    class Meta:
        model = Lab_test

        fields = [
            'name',
            'age',
            'gender',
            'phone',
            'email',
            'address'
        ]

        widgets = {

            'name': forms.TextInput(attrs={
                'placeholder': 'Enter patient name'
            }),

            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter age'
            }),

            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter phone number'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email'
            }),

            'address': forms.Textarea(attrs={
                'placeholder': 'Enter address',
                'rows': 3
            }),
        }


class LabTestForm(forms.ModelForm):

    class Meta:
        model = LabTest

        fields = [
            'test_name',
            'test_code',
            'category',
            'sample_type',
            'normal_range',
            'price',
            'status'
        ]

        widgets = {

            'test_name': forms.TextInput(attrs={
                'placeholder': 'Enter test name'
            }),

            'test_code': forms.TextInput(attrs={
                'placeholder': 'Example: CBC'
            }),

            'normal_range': forms.TextInput(attrs={
                'placeholder': 'Example: 70 - 100 mg/dL'
            }),

            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter price'
            }),
        }