from django.contrib import admin
from .models import Booking, Trainer, Client, Session, Review
# Register your models here.


# booking model
class BookingAdmin(admin.ModelAdmin):
    list_display = ['client', 'session', 'date', 'time', 'review']


admin.site.register(Booking)


# trainer model
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialties']


admin.site.register(Trainer, TrainerAdmin)


# session model
class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'duration', 'price', 'trainer']


admin.site.register(Session, SessionAdmin)


# client model
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'address']


admin.site.register(Client, ClientAdmin)
