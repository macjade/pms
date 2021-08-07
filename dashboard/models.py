from django.db import models
from accounts.models import Doctor
from django.utils import timezone
# Create your models here.

class Prescriptions(models.Model):

    REFILL_CHOICE = [
        ('1 Month', '1 Month'),
        ('3 Month', '3 Month'),
        ('6 Month', '6 Month'),
        ('8 Month', '8 Month'),
        ('12 Month', '12 Month'),
    ]

    rx_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    rx_date = models.DateTimeField(default=timezone.now)
    rx_patient_name = models.CharField(max_length=255)
    rx_drug = models.CharField(max_length=100)
    rx_address = models.CharField(max_length=255)
    rx_description = models.CharField(max_length=1000)
    rx_code = models.CharField(max_length=20)
    rx_amount = models.DecimalField(max_digits=2500, default=0.00, decimal_places=2)
    rx_refill = models.CharField(max_length=20, choices=REFILL_CHOICE, default='1 Month')

    def __str__(self):

        return str(self.rx_doctor.username) + " - " + str(self.rx_patient_name)