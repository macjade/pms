import random

from django.shortcuts import render, redirect
from django.views import generic
from .models import Prescriptions
from accounts.models import Doctor
# Create your views here.


class HomeView(generic.View):

    def get(self, request):

        if not request.user.is_authenticated:
            return redirect("accounts:home")

        get_rx = Prescriptions.objects.filter(rx_doctor=request.user.pk)

        context = {
            "doctor": request.user.get_full_name,
            "precription": get_rx,
        }

        if request.session.get('error'):
            context['error'] = request.session['error']
            request.session.pop('error')

        return render(request, 'dashboard/dashboard.html', context)


class AddRxView(generic.View):

    def post(self, request):
        d_list = '1234567890'
        n_list = 'qwertyuioplkjhgfdsazxcvbnm'

        newid = ''.join(random.choice(d_list) for i in range(5))
        newmn = ''.join(random.choice(n_list) for i in range(5))

        try:
            amt = float(request.POST["amount"])
        except:
            request.session["error"] = "Invalid amount"
            return redirect('dashboard:home')

        newRx = Prescriptions()
        newRx.rx_doctor = Doctor.objects.get(pk=request.user.pk)
        newRx.rx_patient_name = request.POST["patient"]
        newRx.rx_drug = request.POST["drug"]
        newRx.rx_address = request.POST['address']
        newRx.rx_description = request.POST['rx']
        newRx.rx_refill = request.POST['refill']
        newRx.rx_amount = float(request.POST["amount"])
        newRx.rx_code = newmn+newid
        newRx.save()

        return redirect("dashboard:home")
