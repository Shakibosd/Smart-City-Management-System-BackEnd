from django.db import models
from django.contrib.auth.models import User
from .constants import PAYMENT_STATUS

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS)