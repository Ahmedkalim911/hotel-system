from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('rooms/', views.room_list, name='rooms'),
    path('bookings/', views.booking_list, name='bookings'),
    path('add-booking/', views.add_booking,  name='add_booking'),
    path('edit-booking/<int:pk>/', views.edit_booking,  name='edit_booking'),
    path('delete-booking/<int:pk>/', views.delete_booking, name='delete_booking'),
]
