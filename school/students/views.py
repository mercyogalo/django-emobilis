from django.shortcuts import render, redirect
from .models import Students
from . serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.
def home(request):
    return render(request, 'home.html')

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
    
    