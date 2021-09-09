# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:29:27 2021

@author: Sandora
"""

from ctypes import *
from array import array
from Elveflow64 import *


def set_air_pressure(Instr_ID, Calib, pressure_high,channel):
    set_channel=c_int32(channel) # convert to c_int32
    set_pressure=c_double(float(pressure_high) )#convert to c_double
    error=OB1_Set_Press(Instr_ID.value, set_channel, set_pressure, byref(Calib),1000) 
    return error