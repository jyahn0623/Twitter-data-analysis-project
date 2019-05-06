from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
def index(request):
    return render(request, 'helper/index.html', {})

def room(request, room_num):
    return render(request, 'helper/room.html', {
        'room_name' : mark_safe(json.dumps(room_num)),
    })