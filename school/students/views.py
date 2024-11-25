from django.shortcuts import render, redirect
from .models import Students
from . serializers import StudentSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from . credentials import MpesaAccessToken, MpesaPassword

# Create your views here.
def home(request):
    return render(request, 'home.html')

def pay(request):
    return render(request,'pay.html')
    
def students(request):
    if request.method == 'POST':
        phone=request.POST['phone']
        amount=request.POST['amount']
        access_token=MpesaAccessToken.mpesa_access_token
        api_url='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {"Authorization": "Bearer %s" % access_token}
        request={    
   "BusinessShortCode": MpesaPassword.business_short_code,    
   "Password": MpesaPassword.decode_password,    
   "Timestamp":MpesaPassword.lipa-time,    
   "TransactionType": "CustomerPayBillOnline",    
   "Amount": amount,    
   "PartyA":phone,    
   "PartyB":MpesaPassword.business_short_code,    
   "PhoneNumber":phone,    
   "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa",    
   "AccountReference":"Test",    
   "TransactionDesc":"Test"
}
    
    return HttpResponse(success)
    
    

def form(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        image = request.FILES['image']
        
        student = Students(name=name, email=email, phone=phone, age=age, image=image)
        student.save()
        return redirect('./')  # Redirect after saving

    return render(request, 'form.html')  # Correctly indented, within the form function

def formdata(request):
    students = Students.objects.all()
    return render(request, 'formdata.html', {'students': students})


class StudentView(viewsets.ModelViewSet):
    queryset=Students.objects.all()
    serializer_class= StudentSerializer
    
    