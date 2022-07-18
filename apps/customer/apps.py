import oscar.apps.customer.apps as apps
from django.urls import path
from django.utils.translation import gettext_lazy as _

from oscar.core.application import OscarConfig
from oscar.core.loading import get_class

class CustomerConfig(apps.CustomerConfig):
    name = 'apps.customer'

    def ready(self):
        self.cont_view = get_class('customer.views', 'ContView')
        self.login_view = get_class('customer.views', 'AccountAuthView')

    def get_urls(self):
        urls = [
            # Login, logout and register doesn't require login
            path('contact/', self.cont_view.as_view(), name='contact'),
            path('login/', self.login_view.as_view(), name='login'),
            
        ]

        return self.post_process_urls(urls)









    
   
