from django.db import models
from oscar.apps.partner.abstract_models import AbstractPartner

class Partner(AbstractPartner):
    company = models.CharField(max_length=40,blank=True,null=True)






from oscar.apps.partner.models import *  # noqa isort:skip
