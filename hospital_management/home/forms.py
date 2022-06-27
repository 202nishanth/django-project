from cProfile import label
from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'Booking_date': DateInput()
        }

        labels = {
            'Patient_name' : "Patient Name:",
            'Patient_phone' : "Patient Phone No:", 
            'Patient_email' : "Patient Email:",
            'Doc_name' : "Doctors Name:",  
            'Booking_date' : "Booking Date:",
            
        }