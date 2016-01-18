from django.db import models

from django.contrib.auth.models import User


USER_TYPES = (
    ('PATIENT', 'Patients or drug buyers'),
    ('PHARMACISTS', 'Drug store owner')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    category = models.CharField(max_length=50,
                                choices=USER_TYPES, default='PATIENT')

