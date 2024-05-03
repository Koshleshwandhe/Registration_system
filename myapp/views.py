import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .authentication import generate_auth_token

def login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # Generate the base64 authentication token
        auth_token = generate_auth_token(id, password)

        # Make a GET request to the API endpoint with the obtained token
        url = f"https://centrum-backend.vercel.app/login/{user_type}/dashboard/ALL"
        headers = {'Authorization': f'Basic {auth_token}'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Authentication successful, redirect to main screen
            data = response.json()
            return render(request, 'main_screen.html', {'data': data})
        else:
            # Authentication failed, return error message
            return HttpResponse("Invalid username or password.")
    return render(request, "login.html")

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
