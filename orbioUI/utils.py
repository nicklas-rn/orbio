from .views import *


def pcr_cycle():
    steppers.write(bytes(f"upperLayer,1,10,1,", 'utf-8'))
    steppers.write(bytes(f"lowerLayer,-1,10,1,", 'utf-8'))
    steppers.write(bytes(f"diskMotor,1,10,1,", 'utf-8'))
    steppers.write(bytes(f"upperLayer,-1,10,1,", 'utf-8'))
    steppers.write(bytes(f"lowerLayer,1,10,1,", 'utf-8'))


def open_disk_lifter():
    steppers.write(bytes(f"lifter,1,100,1,", 'utf-8'))


def insert_disk():
    steppers.write(bytes(f"lifter,-1,100,1,", 'utf-8'))
