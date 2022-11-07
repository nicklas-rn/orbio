from django.shortcuts import render
from .models import *
import time, json, serial
from django.http import HttpResponse

try:
    steppers = serial.Serial(port='/dev/cu.usbserial-1120', baudrate=115200, timeout=.1)
except:
    steppers = serial.Serial()


def home(request):

    context = {}

    return render(request, 'orbioUI/home.html', context)


def developer(request):

    context = {}

    return render(request, 'orbioUI/developer.html', context)


def move_element(request):

    element = json.loads(request.POST['element'])
    dir = json.loads(request.POST['dir'])
    steps = json.loads(request.POST['steps'])

    print(element, dir, steps)

    steppers.write(bytes(f"{element},{dir},{steps},", 'utf-8'))

    response = json.dumps({
        'status': 'ok',
    })

    return HttpResponse(response)


def home_elements(request):

    steppers.write(bytes(f"homeElements", 'utf-8'))

    response = json.dumps({
        'status': 'ok',
    })

    return HttpResponse(response)

