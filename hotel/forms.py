from django import forms
from .models import Booking, Room, Customer

class BookingForm(forms.ModelForm):
    class Meta:
        model  = Booking
        fields = ['customer', 'room', 'check_in', 'check_out', 'total_price']
        widgets = {
            'check_in':  forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }