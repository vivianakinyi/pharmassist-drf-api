from django.db import models

from django.contrib.auth.models import AbstractBaseUser


class Patient(AbstractBaseUser):
    """
    Stores patient details
    """
    id = models.UUIDField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(verbose_name='email_address',
                              max_length=255,
                              unique=True)

    def __str__(self):
        return self.email


class Pharmacist(AbstractBaseUser):
    """
    Stores pharmacists details
    """
    id = models.UUIDField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(verbose_name='email_address',
                              max_length=255,
                              unique=True)

    def __str__(self):
        return self.email
