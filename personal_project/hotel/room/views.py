from django.shortcuts import render
from .models import Room
# Create your views here.

def welcome(request):
    return render(request, 'hotel_welcome.html')

def roomList(request):
    rooms = Room.objects.all()
    return render(request, 'hotel_rooms.html', {'rooms': rooms})