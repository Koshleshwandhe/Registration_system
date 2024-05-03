import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .authentication import generate_auth_token

import requests
from django.shortcuts import render

def fetch_customer_data():
    # Make a GET request to the open-source API to fetch customer data
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def login(request):
    if request.method == 'GET':
        # Fetch customer data
        customers = fetch_customer_data()   
        return render(request, 'customer_list.html', {'customers': customers})
    else:
        return HttpResponse("Invalid request method")

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
    # Render the main screen template without data initially
    return render(request, 'main_screen.html')
