from django.shortcuts import render

# Create your views here.


from django.utils import timezone
from django.http import HttpResponse

from .models import Doctor
from .models import Patient
from django.shortcuts import render, redirect, get_object_or_404
from .models import HospitalBill, BillService

def dashboard(request):

    total = Patient.objects.count()
    total_d = Doctor.objects.count()

    admitted = Patient.objects.count()

    discharged = Patient.objects.count()

    context = {
        "total": total,
        "admitted": admitted,
        "discharged": discharged,
        "total1": total_d,
    }
    return render(request, "dashboard.html", context)


def add_patient(request):
    if request.method == "POST":
        Patient_Id=request.POST.get("P_id")
        Patient_first_name=request.POST.get("First_name")
        Patient_last_name =request.POST.get("Last_name")
        Pateint_phone=request.POST.get("phone")
        Patient_address = request.POST.get("address")
        Patient_age = request.POST.get("age")
        P_gender = request.POST.get("gender")
        P_father_name = request.POST.get("Father_name")
        Pateint_Date =request.POST.get("P_date")
        Patient_Email =request.POST.get("email")
        Patient_Bade =request.POST.get("P_bade")
        P_Ward=request.POST.get("P_Ward")
        P_admission_date = request.POST.get("P_admission")
        Patient_Iamge = request.FILES["image"]
        Patient( first_name=Patient_first_name,last_name=Patient_last_name,patient_id=Patient_Id,
                father_name=P_father_name
                , gender=P_gender,dob=Pateint_Date, age=Patient_age,mobile=Pateint_phone,email=Patient_Email,
                address=Patient_address,
                ward=P_Ward, bed_no=Patient_Bade, admission_date=P_admission_date, photo=Patient_Iamge).save()

    users = Patient.objects.all()

    return render(request, "add_patient.html", {"users":users})


def patient_list(request):

    patients = Patient.objects.all().order_by("-id")

    return render(
        request,
        "patient_list.html",
        {
            "patients": patients
        }
    )

def edit_patient(request, id):

    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":

        Pateint_id = request.POST.get("P_id")
        Patient_first_name = request.POST.get("First_name")
        Patient_last_name = request.POST.get("Last_name")
        Pateint_phone = request.POST.get("phone")
        Patient_address = request.POST.get("address")
        Patient_age = request.POST.get("age")
        P_gender = request.POST.get("gender")
        P_father_name=request.POST.get("Father_name")
        Pateint_Date = request.POST.get("P_date")
        Patient_Email= request.POST.get("email")
        Patient_Bade = request.POST.get("P_bade")
        P_Ward  = request.POST.get("P_Ward")
        P_admission_date = request.POST.get("P_admission")
        Patient_Iamge=request.FILES["image"]
        Patient(patient_id=Pateint_id,first_name=Patient_first_name,last_name=Patient_last_name,father_name=P_father_name
                ,gender=P_gender,dob=Pateint_Date,age=Patient_age,mobile=Pateint_phone,email=Patient_Email,address=Patient_address,
                ward=P_Ward,bed_no=Patient_Bade,admission_date=P_admission_date,photo=Patient_Iamge).save()
        X=Patient.objects.all.filter(first_name=Patient_first_name,last_name=Patient_last_name)
        if X == 1:
            return HttpResponse("<script>alert('your are arledy register');location.href='/register/'</script>")

        return redirect("patient_list")

    return render(request, "edit_patient.html", {"patient": patient})

def profile(request):

    users=Patient.objects.all()
    return render(request,'patient_list.html',{'users':users})

def Appointment(request):
    doctors = Doctor.objects.all().order_by("id")
    Radiology=Doctor.objects.filter(specialization="Radiology")
    Physical = Doctor.objects.filter(specialization="Physical")
    cardiology = Doctor.objects.filter(specialization="Cardiology")



    return render(request,'Appointments.html',

                  {"Radiology":Radiology,
                   "Physical":Physical,
                   "cardiology":cardiology,
                   "doctors": doctors,


                   }       )



def doctor_list(request):
    if request.method == "POST":
        Docor_F_name=request.POST.get('Dr_first_name')
        Doctor_quali=request.POST.get('Dr_Qualification')
        Docor_email = request.POST.get('Dr_email')
        Docor_Exe = request.POST.get('Expreince')
        Docor_Phone = request.POST.get('Number')
        Docor_Spe = request.POST.get('specialization')
        Stauts = request.POST.get('Status')
        Docor_image = request.FILES['Image']
        Doctor( name =Docor_F_name,email=Docor_email,phone=Docor_Phone,status = Stauts,image=Docor_image,qualification=Doctor_quali,experience=Docor_Exe, specialization=Docor_Spe).save()
    doctors = Doctor.objects.all().order_by("id")
    x=Doctor.objects.all().count()
    print(x)
    if x==1:
        print("hello")
    else:
        print("hii")
    return render(request, "doctor.html", {"doctors": doctors})
def Show_d(request):
    doctors = Doctor.objects.all().order_by("-id")


    return render(request,'view.html',{'doctors':doctors}
        )

def Delete(request,id):
    patient_d=Patient.objects.all()
    patient_d.delete()
    return render(request,"patient_list.html")

def Doctor_d(request,id):
    doctor=Doctor.objects.all()
    doctor.delete()
    return render(request,"view.html")


def Bill_ditail(request):

    return render(request,'billing_details.html')

def Search(request):
    query = request.GET.get('search', '')

    if query:
        patients = Patient.objects.filter(
            first_name__icontains=query
        ) | Patient.objects.filter(
            last_name__icontains=query
        ) | Patient.objects.filter(
            patient_id__icontains=query
        ) | Patient.objects.filter(
            mobile__icontains=query
        )
    else:
        patients = Patient.objects.all()

    context = {
        'patients': patients,
        'query': query,
    }

    return render(request, 'patient_list.html', context)




def create_bill(request):

    if request.method == "POST":

        # -------------------------
        # PATIENT DETAILS
        # -------------------------

        ipno = request.POST.get("ipno")
        uhid = request.POST.get("uhid")
        bill_no = request.POST.get("bill_no")

        patient_name = request.POST.get("patient_name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")

        relation_name = request.POST.get("relation_name")
        room_bed = request.POST.get("room_bed")
        doctor = request.POST.get("doctor")
        category = request.POST.get("category")


        # -------------------------
        # DATE DETAILS
        # -------------------------

        bill_date = request.POST.get("bill_date")
        bill_time = request.POST.get("bill_time")

        admission_date = request.POST.get("admission_date")
        admission_time = request.POST.get("admission_time")

        discharge_date = request.POST.get("discharge_date")
        discharge_time = request.POST.get("discharge_time")


        # -------------------------
        # PAYMENT
        # -------------------------

        discount = request.POST.get("discount") or 0
        advance = request.POST.get("advance") or 0
        paid = request.POST.get("paid") or 0


        # -------------------------
        # SERVICES
        # -------------------------

        service_names = request.POST.getlist("service_name[]")
        rates = request.POST.getlist("rate[]")
        counts = request.POST.getlist("count[]")
        totals = request.POST.getlist("total[]")


        # -------------------------
        # GROSS AMOUNT
        # -------------------------

        gross_amount = 0

        for total in totals:

            if total:
                gross_amount += float(total)


        # -------------------------
        # NET AMOUNT
        # -------------------------

        net_amount = (
            gross_amount - float(discount)
        )


        # -------------------------
        # BALANCE
        # -------------------------

        balance = (
            net_amount
            - float(advance)
            - float(paid)
        )


        if balance < 0:
            balance = 0


        # -------------------------
        # SAVE BILL
        # -------------------------

        bill = HospitalBill.objects.create(

            ipno=ipno,
            uhid=uhid,
            bill_no=bill_no,

            patient_name=patient_name,
            age=age,
            gender=gender,

            relation_name=relation_name,
            room_bed=room_bed,
            doctor=doctor,
            category=category,

            bill_date=bill_date,
            bill_time=bill_time,

            admission_date=admission_date,
            admission_time=admission_time,

            discharge_date=discharge_date or None,
            discharge_time=discharge_time or None,

            discount=discount,
            advance=advance,
            paid=paid,

            gross_amount=gross_amount,
            net_amount=net_amount,
            balance=balance
        ).save()


        # -------------------------
        # SAVE SERVICES
        # -------------------------

        for i in range(len(service_names)):

            if not service_names[i]:
                continue

            BillService.objects.create(

                bill=bill,

                service_name=service_names[i],

                rate=rates[i] or 0,

                count=counts[i] or 1,

                total=totals[i] or 0
            ).save()


        print(bill)   # Bill page par bhejna

        return redirect(
            "Bill_ditail",

        )


    return render(
        request,
        "billing.html"
    )

def Home(request):
    return render(request,'index.html')

def help_center(request):
    return render(request, "help_center.html")

# lab test start ---------------------------------------------------------------------------------------------


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Lab_test, LabTest
from .forms import Lab_testForm, LabTestForm


def lab_tests(request):

    tests = LabTest.objects.all().order_by('-id')
    patients = Lab_test.objects.all().order_by('-id')

    search = request.GET.get('search', '')
    category = request.GET.get('category', '')
    status = request.GET.get('status', '')

    if search:
        tests = tests.filter(test_name__icontains=search)

    if category:
        tests = tests.filter(category=category)

    if status == 'active':
        tests = tests.filter(status=True)

    elif status == 'inactive':
        tests = tests.filter(status=False)

    patient_form = Lab_testForm()
    test_form = LabTestForm()

    context = {
        'tests': tests,
        'patients': patients,
        'patient_form': patient_form,
        'test_form': test_form,
        'total_patients': Patient.objects.count(),
        'total_tests': LabTest.objects.count(),
    }

    return render(
        request,
        'lab/lab_test.html',
        context
    )


def Add_patient(request):

    if request.method == 'POST':

        form = Lab_testForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Patient added successfully!'
            )

        else:

            messages.error(
                request,
                'Please check patient details.'
            )

    return redirect('lab_tests')


def add_lab_test(request):

    if request.method == 'POST':

        form = LabTestForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Lab test added successfully!'
            )

        else:

            messages.error(
                request,
                'Please check lab test details.'
            )

    return redirect('lab_tests')


def delete_lab_test(request, pk):

    test = get_object_or_404(
        LabTest,
        pk=pk
    )

    test.delete()

    messages.success(
        request,
        'Lab test deleted successfully!'
    )

    return redirect('lab_tests')


def edit_lab_test(request, pk):

    test = get_object_or_404(
        LabTest,
        pk=pk
    )

    if request.method == 'POST':

        form = LabTestForm(
            request.POST,
            instance=test
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Lab test updated successfully!'
            )

            return redirect('lab_tests')

    else:

        form = LabTestForm(instance=test)

    return render(
        request,
        'lab/Edit_test.html',
        {
            'form': form,
            'test': test
        }
    )

def Demo(request):
    doctor_profile=Doctor.objects.all()
    return render(request,'doctor_profile.html',{'doctor':doctor_profile})

def About(request):
    return render(request ,'about.html')

def Contact(request):
    return render(request,'contact.html')
def Service(request):
    return  render(request,'service.html')
def Labratory(request):
    return render(request,'labratory/labratory_dasboard.html')
def Labratory_doctor(request):
    return render(request,'labratory/labratory_doctor.html')
def Labratory_addpatente(request):
    return render(request,'labratory/labratory_Addpanteint.html')
def temprory(request):
    return HttpResponse("hello this is my page ")
   