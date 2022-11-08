from django.shortcuts import render
from .models import *
import time, json, serial
from django.http import HttpResponse

try:
    steppers = serial.Serial(port='/dev/cu.usbserial-1120', baudrate=115200, timeout=.1)
except:
    steppers = serial.Serial()


try:
    heaters = serial.Serial(port='/dev/cu.usbserial-1130', baudrate=115200, timeout=.1)
except:
    heaters = serial.Serial()


def home(request):

    context = {}

    return render(request, 'orbioUI/home.html', context)


def developer(request):

    context = {}

    return render(request, 'orbioUI/developer.html', context)


def developer_moveSteppers(request):

    context = {}

    return render(request, 'orbioUI/developer_moveSteppers.html', context)


def developer_setHeaters(request):

    context = {}

    return render(request, 'orbioUI/developer_setHeaters.html', context)


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


def read_temps(request):

    temps = str(heaters.readline()).split(',')

    response = json.dumps({
        'status': 'ok',
        'temps': temps,
    })

    return HttpResponse(response)



