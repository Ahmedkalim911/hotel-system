from django.shortcuts import render,redirect
from .models import Room, Booking, Customer
from .forms import  BookingForm
from django.shortcuts import render, redirect, get_object_or_404

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/rooms.html', {'rooms': rooms})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'hotel/bookings.html', {'bookings': bookings})
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            # خلي الغرفة غير متاحة
            room = booking.room
            room.is_available = False
            room.save()
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, 'hotel/add_booking.html', {'form': form})



def edit_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'hotel/add_booking.html', {'form': form})

def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        room = booking.room
        room.is_available = True
        room.save()
        booking.delete()
        return redirect('bookings')
    return render(request, 'hotel/delete_booking.html', {'booking': booking})

def home(request):
    total_rooms    = Room.objects.count()
    available      = Room.objects.filter(is_available=True).count()
    total_bookings = Booking.objects.count()
    return render(request, 'hotel/home.html', {
        'total_rooms':    total_rooms,
        'available':      available,
        'total_bookings': total_bookings,
    })

