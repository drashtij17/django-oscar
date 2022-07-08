from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    place = models.CharField(max_length=40,blank=True,null=True)



from oscar.apps.catalogue.models import *  # noqa isort:skip
