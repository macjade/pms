from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.views import generic
from .models import Doctor

import base64
import random

class HomeView(generic.View):

    def get(self, request):
        return redirect('accounts:login')

class LoginView(generic.View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("dashboard:home")
        return render(request, 'accounts/login.html')

    def post(self, request):
        user = authenticate(username=request.POST["email"], password=request.POST["password"])

        if user is not None:
            request.session.set_expiry(0)

            login(self.request, user)

            return redirect('dashboard:home')

        return (redirect("accounts:login"))

class RegisterView(generic.View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("dashboard:home")
        return render(request, 'accounts/register.html')
    
    def post(self, request):

        check_email = Doctor.objects.filter(email=request.POST["email"]).exists()
        d_list = '1234567890'
        context = {
        }
        if not check_email:
            d_name = str(request.POST["firstname"])
            newid = ''.join(random.choice(d_list) for i in range(5))
            new_user = Doctor()
            new_user.firstname = request.POST["firstname"]
            new_user.lastname = request.POST["lastname"]
            new_user.username = d_name + newid
            new_user.email = request.POST["email"]
            new_user.hospital_name = request.POST["hospitalname"]
            password = request.POST["password"]
            new_user.set_password(password)
            new_user.save()

            user = authenticate(username=request.POST["email"], password=request.POST["password"])

            if user is not None:
                request.session.set_expiry(0)
                login(self.request, user)

                return redirect('dashboard:home')

            return (redirect("accounts:register"))

        return (redirect("accounts:register"))


def logoutview(request):
    logout(request)
    return redirect("home:home")