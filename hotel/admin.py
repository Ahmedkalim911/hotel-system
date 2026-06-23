from django.contrib import admin
from .models import Room, Booking, Customer
# Register your models here.
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Customer)