from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.models import User
from bookings.models import Client


class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "bookings/dashboard/{id}"
        return path.format(id=request.user.id)

    def confirm_email(self, request, email_address):
        user_record = User.objects.get(emailaddress=email_address)
        try:
            client = Client.objects.get(user=user_record)
        except Exception:
            newClient = Client(user=user_record)
            newClient.save()
        return super().confirm_email(request, email_address)
