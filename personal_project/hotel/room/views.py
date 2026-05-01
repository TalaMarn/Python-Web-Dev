from django.shortcuts import render
from .models import Room
from django.core.paginator import Paginator

# Create your views here.

def welcome(request):
    rooms = Room.objects.all().order_by('id')[:3]
    context = {
        'rooms': rooms,
    }

    return render(request, 'hotel_welcome.html', context)

def roomList(request):
    query = request.GET.get('q')
    if query:
        rooms = Room.objects.filter(roomType__icontains=query)
    else:
        rooms = Room.objects.all()

    paginator = Paginator(rooms, 9)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    return render(request, 'hotel_rooms.html', {'rooms': page_obj})