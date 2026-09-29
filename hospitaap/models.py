
# Create your models here.
from django.db import models
from datetime import date

class Patient(models.Model):
    patient_id = models.CharField(max_length=50, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ]
    )

    dob = models.DateField()
    age = models.PositiveIntegerField()

    mobile = models.CharField(max_length=15)


    email = models.EmailField(blank=True)

    address = models.TextField()



    department = models.CharField(max_length=100)


    disease = models.TextField()

    ward = models.CharField(max_length=100,null='0')
    bed_no = models.CharField(max_length=20)

    admission_date = models.DateField(default=date.today)


    status = models.CharField(
        max_length=20,
        default="Admitted"
    )

    photo = models.ImageField(
        upload_to="patients/",
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.patient_id:
            name = self.first_name[:3].upper()  # पहले 3 अक्षर
            dob = self.dob.strftime("%d%m%Y")  # 15082000
            age = str(self.age)  # 26

            self.patient_id = f"{name}{dob}{age}"

        super().save(*args, **kwargs)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    qualification = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(upload_to='doctor_images/')
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Busy', 'Busy'),
        ('On Leave', 'On Leave'),
        ('Offline', 'Offline'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    def __str__(self):
        return self.name







class HospitalBill(models.Model):

    # Patient Details
    ipno = models.CharField(max_length=50)
    uhid = models.CharField(max_length=100,null='')
    bill_no = models.CharField(max_length=50,null='' )

    patient_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=20,
        choices=[
            ("MALE", "Male"),
            ("FEMALE", "Female"),
            ("OTHER", "Other"),
        ]
    )

    relation_name = models.CharField(max_length=200, blank=True)

    room_bed = models.CharField(
        max_length=100,
        blank=True
    )

    doctor = models.CharField(
        max_length=200,
        blank=True
    )

    category = models.CharField(
        max_length=50,
        default="PAYMENT"
    )

    # Dates
    bill_date = models.DateField()
    bill_time = models.TimeField()

    admission_date = models.DateField()
    admission_time = models.TimeField()

    discharge_date = models.DateField(
        null=True,
        blank=True
    )

    discharge_time = models.TimeField(
        null=True,
        blank=True
    )

    # Payment
    discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    advance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    paid = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    gross_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    net_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.bill_no} - {self.patient_name}"


class BillService(models.Model):

    bill = models.ForeignKey(
        HospitalBill,
        on_delete=models.CASCADE,
        related_name="services"
    )

    service_name = models.CharField(
        max_length=200
    )

    rate = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    count = models.PositiveIntegerField(
        default=1
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return self.service_name





class Lab_test(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LabTest(models.Model):

    CATEGORY_CHOICES = [
        ('Hematology', 'Hematology'),
        ('Biochemistry', 'Biochemistry'),
        ('Pathology', 'Pathology'),
        ('Immunology', 'Immunology'),
    ]

    SAMPLE_CHOICES = [
        ('Whole Blood', 'Whole Blood'),
        ('Serum', 'Serum'),
        ('Plasma', 'Plasma'),
        ('Urine', 'Urine'),
        ('Other', 'Other'),
    ]

    test_name = models.CharField(max_length=200)
    test_code = models.CharField(max_length=50)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    sample_type = models.CharField(
        max_length=50,
        choices=SAMPLE_CHOICES
    )
    normal_range = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.test_name


