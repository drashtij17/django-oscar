from django.db import models
from oscar.apps.partner.abstract_models import AbstractPartner

class Partner(AbstractPartner):
    company = models.CharField(max_length=40,blank=True,null=True)


class Information(models.Model):
    income = models.CharField(max_length=30,null=True,blank=True)

from oscar.apps.partner.models import *  
