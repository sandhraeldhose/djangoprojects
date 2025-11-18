from django.db import models
import random
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(null=True)
    otp=models.CharField(null=True,blank=True)
    is_verified=models.BooleanField(default=False)


    #after registrartion user object calls

    def generate_otp(self):
        otp=str(random.randint(1000,9999))+str(self.id)
        self.otp=otp
        self.save()


