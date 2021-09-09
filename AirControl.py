# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:48:49 2021

@author: Sandora
"""

import sys
from email.header import UTF8
sys.path.append("C:\\Users\\OceanSpectro\\Desktop\\Sandra\\Air controller\\SDK_V3_05_03\\Python_64\\DLL64")#add the path of the library here
sys.path.append("C:\\Users\\OceanSpectro\\Desktop\\Sandra\\Air controller\\SDK_V3_05_03\\Python_64") #add the path of the LoadElveflow.py

from ctypes import *
from array import array
from Elveflow64 import *
import time
from AirControlFunctions import *

# USER PARAMETERS
pressure_high = 2000 # mbar
pressure_low = 0



# Initialization of OB1
Instr_ID=c_int32()
#see User Guide to determine regulator types and NIMAX to determine the instrument name 
error=OB1_Initialization('01C3577F'.encode('ascii'),1,2,4,3,byref(Instr_ID)) 
#all functions will return error codes to help you to debug your code, for further information refer to User Guide
print('error:%d' % error)
print("OB1 ID: %d" % Instr_ID.value)


# Set the calibration type as default
Calib=(c_double*1000)()#always define array this way, calibration should have 1000 elements
error=Elveflow_Calibration_Default (byref(Calib),1000)


# Set pressure to 2 bars
set_air_pressure(Instr_ID, Calib, pressure_high,2)
time.sleep(5)
set_air_pressure(Instr_ID, Calib, pressure_low,2)

       
#  CLOSE THE CONNECTION
error=OB1_Destructor(Instr_ID.value)