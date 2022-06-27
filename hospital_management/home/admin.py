from django.contrib import admin
from .models import Booking, departments,Doctors,Booking

# Register your models here.
admin.site.register(departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'Patient_name', 'Patient_phone', 'Patient_email', 'Doc_name', 'Booking_date', 'Booked_on')

admin.site.register(Booking, BookingAdmin)

