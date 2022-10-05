from django.shortcuts import redirect, render
from datetime import date
from xmlrpc.client import DateTime
#from HospitalApp.models.HospitalAuthModel import *
from django.contrib import messages

from HospitalApp.models.HospitalAuthModel import tbl_hospital_register
from HospitalApp.models.PatientModel import tbl_patient_information
from django.contrib.auth import authenticate, logout, login as auth_login

def Add_PersonalInfo(request): 
    if request.method == "POST":
        AadhaarID = request.POST.get('AadhaarId')
        AadhaarID =AadhaarID.replace('-', '')
        
        pname = request.POST.get('pname')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        bgroup = request.POST.get('bloodgroup')
        bpressure = request.POST.get('bp')
        diabetes = request.POST.get('Diabetes')
        colestrol = request.POST.get('Colestrol')

        fdoc = request.POST.get('fdoc')
        fdocnumber = request.POST.get('fdocnumber')
        allergies = request.POST.get('Allergies')
        surgery = request.POST.get('Surgery')
        category = request.POST.get('category')
        AddedBy = request.session['loggedin_user']  


        if tbl_patient_information.objects.filter(AadhaarId=AadhaarID).first():
                messages.warning(request, 'Patient data already added!')
                return redirect('/disease')
        else:
            patient_obj = tbl_patient_information.objects.create( AadhaarId = AadhaarID,
                        name =pname,number =  phone,dob = dob,gender = gender,category=category,address = address,bloodgroup = bgroup,bloodpressure = bpressure,diabetes=diabetes,colestrol = colestrol,
                        familydoctor_name =fdoc,    doctor_number = fdocnumber,allergies = allergies,surgeryhistory = surgery, AddedBy=AddedBy)
            patient_obj.save()
          

            messages.success(request, "Data Added Successfully")
               
            return render(request, 'dashboard/patient-personal-info.html')
        
            

      
    return render(request, 'dashboard/patient-personal-info.html')

  

  