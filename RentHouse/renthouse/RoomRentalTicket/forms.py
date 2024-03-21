from django import forms
from .models import RoomRentalTicket 

class RoomRentalTicketForm(forms.ModelForm): 
    class Meta:
        model = RoomRentalTicket
        fields = '__all__'
