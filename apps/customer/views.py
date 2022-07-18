# from oscar.apps.customer.views import ProfileView

# class Proflie(ProfileView):
#     template_name = 'oscar/customer/profile/profile.html'

from django.views import generic

class ContView(generic.TemplateView):
    
    template_name = 'oscar/customer/contact.html'


