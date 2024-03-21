from django.db import models
from PaymentMethods.models import PaymentMethods
from account.models import Account
from Room.models import Room

class RoomRentalTicket(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    paymentmethods = models.ForeignKey(PaymentMethods, on_delete=models.CASCADE)

    def __str__(self):
        return f"Room Rental Ticket #{self.id} - Room: {self.room}, Account: {self.account}, Payment Method: {self.paymentmethods}"

