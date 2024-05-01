from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('password')
        user = User.objects.filter(id=id, password=password).first()
        if user:
            return render(request,'main_screen.html')
        else:
            return HttpResponse("Invalid username or password.'")
    return render(request,"login.html")

def signin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        new_user = User.objects.create(name=name, id=id, password=password, phone_number=phone_number, email=email)
        new_user.save()
        return redirect('login')
    return render(request,"signin.html")

def main_screen(request):
    return render(request,"main_screen.html")