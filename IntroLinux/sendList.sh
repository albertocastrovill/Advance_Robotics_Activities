#!/bin/bash

# Define the list of numbers as comma separated string values
listOfNumbers="45,67,56,33,78,23"

#CAll the Python script with the list of numbers as an argument
python_script="/home/albertocastro/Documents/UDEM/RoboticaAvanzada/Activities/IntroLinux/largestNumber.py"
python3 "$python_script" "$listOfNumbers"