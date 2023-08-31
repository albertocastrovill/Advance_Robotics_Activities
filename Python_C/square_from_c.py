#import all names from ctypes
from ctypes import *

#assign the path to the shared library 
soFile = "/home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/Python_C/squareOfNumber.so"

#load the shared library specified by soFile
squareOfNumber = CDLL(soFile)

print(type(squareOfNumber))

#Call square function from the shared library passing number int
print(squareOfNumber.square(10))

print("Done")