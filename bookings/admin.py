from django.contrib import admin
from .models import Booking
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ['client', 'session', 'date', 'time']


admin.site.register(Booking)
