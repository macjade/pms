from django.shortcuts import render, redirect
from django.views import generic
from django.http import JsonResponse
from dashboard.models import Prescriptions


# Create your views here.

class HomeView(generic.View):

    def get(self, request):
        context = {

        }

        if request.session.get('get_rx'):
            context['rx'] = request.session['get_rx']
            request.session.pop('get_rx')

        if request.session.get('error_msg'):
            context['error_msg'] = request.session['error_msg']
            request.session.pop('error_msg')
        print(context)
        return render(request, 'home/index.html', context)

class GetRX(generic.View):

    def get(self, request, *args, **kwargs):

        try:
            if Prescriptions.objects.filter(rx_code=kwargs.get('code')).exists():
                get_rx = Prescriptions.objects.get(rx_code=kwargs.get('code'))

                data = [str(get_rx.rx_date), str(get_rx.rx_patient_name), str(get_rx.rx_drug), str(get_rx.rx_address), str(get_rx.rx_refill), str(get_rx.rx_amount), str(get_rx.rx_doctor.get_full_name())]

                return JsonResponse({
                    'data': data,
                    'success': 'Successful',
                })
            else:
                return JsonResponse({
                    'error': 'Invalid Rx code',
                })
        except:
           return JsonResponse({
               'error': 'Unable to validate your code. Please try again later.',
           })