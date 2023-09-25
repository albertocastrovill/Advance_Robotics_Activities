import math

class Wheel:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.circunference = 2 * math.pi * radius

class WheelSpeed:
    def __init__(self, ratePulsesToEncoder):
        self.revolutionsPerSecond = ratePulsesToEncoder
        self.angularSpeed = ratePulsesToEncoder*2*math.pi
        self.linearSpeed = ratePulsesToEncoder* myWheel.circunference
    #def update(self, newRevolutionPerSecond, new)

def calculateDistance(currentLinearSpeed, deltaTime):
    distance = currentLinearSpeed *deltaTime
    return distance


inputRadius = float(input("Enter the whele radius in meters: "))
inputEncoder = float(input("Enter Encoder Resolution: "))
inputPulses = float(input("Enter Pulses per Revolution per Unit Time (s): "))
timeInterval = float(input("Enter Elapsed Time in seconds (s): "))

myWheel = Wheel (inputRadius)
myWheelSpeed = WheelSpeed(inputPulses/inputEncoder)
traveledDistance =calculateDistance(myWheelSpeed.linearSpeed, timeInterval)

print ("Wheel radius: {} meters".format(myWheel.radius))
print ("Wheel diameter: {} meters".format(myWheel.diameter))
print ("Wheel circumference: {} meters".format(myWheel.circunference))
print ("Wheel Speed: {} meters".format(myWheelSpeed.revolutionsPerSecond))
print ("Wheel Angular Speed: {} meters".format(myWheelSpeed.angularSpeed))
print ("Wheel Linear Speed: {} meters".format(myWheelSpeed.linearSpeed))
print ("Wheel Distance traveled with {} pulses:{:.2f}meters".format(inputPulses,traveledDistance))