from django.shortcuts import render
from .models import Room 
from .forms import RoomRentalTicketForm
from .models import PaymentMethods

# Create your views here.

def RoomRentalTicket(request): 
    if request.method == 'POST':
        form = RoomRentalTicketForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save()  
            return redirect('home')
    else:
        form = RoomRentalTicketForm(initial={'account': request.user})
    context = {'form': form}
    return render(request, 'rentalticket/rentalticket.html', context)