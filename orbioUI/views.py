from django.shortcuts import render
from .models import *
from .utils import *
import time, json, serial, re
import serial.tools.list_ports
from django.http import HttpResponse


global steppers
global heaters


def initialize_ports():
    ports = serial.tools.list_ports.comports()

    print([port.name for port in ports])

    global steppers
    global heaters

    try:
        steppers = serial.Serial(port='/dev/cu.usbserial-120', baudrate=115200, timeout=.1)
    except:
        steppers = serial.Serial()


    try:
        heaters = serial.Serial(port='/dev/cu.usbserial-110', baudrate=19200, timeout=.1)
    except:
        heaters = serial.Serial()

    time.sleep(1)


initialize_ports()


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
    speed = json.loads(request.POST['speed'])

    print(element, dir, steps, speed)

    data_received = False

    try:
        steppers.write(bytes(f"{element},{dir},{steps},{speed},", 'utf-8'))
        data_received = True
    except serial.serialutil.PortNotOpenError:
        print('Serial port not available (moving element)')
        initialize_ports()

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
        temps = re.sub('[^\d\.\,]', '', str(heaters.readline())).split(',')
        print(temps)
    except serial.serialutil.PortNotOpenError:
        print('Serial port not available (reading temp)')
        temps = ['0', '0', '0', '0']
        initialize_ports()

    response = json.dumps({
        'status': 'ok',
        'temps': json.dumps(temps),
    })

    if len(temps) == 4:
        try:
            return HttpResponse(response)
        except ValueError:
            print('wrong data received')


def set_temps(request):

    temps = json.loads(request.POST['temps'])

    try:
        heaters.write(bytes(f"{temps[0]},{temps[1]},{temps[2]},{temps[3]},", 'utf-8'))
    except:
        print('Serial port not available')

    response = json.dumps({
        'status': 'ok',
    })

    return HttpResponse(response)


def production(request):

    context = {}

    return render(request, 'orbioUI/production.html', context)


def pcr_run(request):

    context = {}

    return render(request, 'orbioUI/pcr_run.html', context)

