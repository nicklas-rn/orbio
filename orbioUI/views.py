from django.shortcuts import render
from .models import *
import time, json, serial
import serial.tools.list_ports
from django.http import HttpResponse

ports = serial.tools.list_ports.comports()

print([port.name for port in ports])

try:
    steppers = serial.Serial(port='ttyUSB0', baudrate=115200, timeout=.1)
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

    try:
        temps = str(heaters.readline()).split(',')
    except:
        print('Serial port not available')
        temps = ['0', '0', '0', '0']

    response = json.dumps({
        'status': 'ok',
        'temps': json.dumps(temps),
    })

    return HttpResponse(response)


def set_temps(request):

    temps = json.loads(request.POST['temps'])

    try:
        heaters.write(bytes(f"{temps[0]},{temps[1]},{temps[2]},,{temps[3]}", 'utf-8'))
    except:
        print('Serial port not available')

    response = json.dumps({
        'status': 'ok',
    })

    return HttpResponse(response)
