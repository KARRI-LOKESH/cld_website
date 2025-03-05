from django.db import models

# Create your models here.
import random
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    rollno = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=15, null=True)
    otp = models.CharField(max_length=6, null=True, blank=True)  # OTP Field

    def generate_otp(self):
        """Generate a 6-digit OTP and save it"""
        self.otp = str(random.randint(100000, 999999))
        self.save()

    def __str__(self):
        return self.email
