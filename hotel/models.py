from django.db import models

class Room(models.Model) :
    ROOM_TYPES = [
        ('single', 'SINGLE'),
        ('double', 'DOUBLE'),
        ('suite', 'SUITE'),
    ]
    number=models.IntegerField(unique=True)
    type=models.CharField(max_length=10, choices=ROOM_TYPES)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.number} ({self.type})"

class Customer(models.Model) :
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    customer   = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room       = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in   = models.DateField()
    check_out  = models.DateField()
    total_price= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking for {self.customer.name} in Room {self.room.number}"