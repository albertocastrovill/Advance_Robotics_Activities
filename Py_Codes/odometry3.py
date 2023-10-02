"""
UDEM
Advanced Robotics

This Python code represents a computing process to calculate odometry in a
single wheel using object oriented programming and structured variables
"""
import math

# Create a class named wheel with the convinient structured variables
class Wheel:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.circumference = 2 * math.pi * radius


class WheelSpeed:
    def __init__(self, ratePulsesToEncoder):
        self.revolutionsPerSecond = ratePulsesToEncoder
        self.angularSpeed = ratePulsesToEncoder*2*math.pi
        self.linearSpeed = ratePulsesToEncoder*myWheel.circumference
    #def update(self, newRevolutionsPerSecond, new)


def calculateDistance(currentLinearSpeed, deltaTime):
    # Calculate the distance traveled based on the number of pulses received
    # Each pulse corresponds to a fraction of the wheel's circumference
    distance = currentLinearSpeed * deltaTime
    return distance

# Ask the user for the wheel radius
inputRadius = float(input("Enter the wheel radius in meters: "))
# Ask the user for the pulses per 1 revolutino available in the Encoder
inputEncoder = float(input("Enter Encoder Resolution: "))
# Ask the user for the accumulated count of pulses in 1 seconds
inputPulses = float(input("Enter Pulses per Revolution per Unit Time (s): "))
# Ask the user for the elapsed time
timeInterval = float(input("Enter Elapsed Time in seconds (s): "))

# Create a Wheel object with the user-provided radius
myWheel = Wheel(inputRadius)
myWheelSpeed = WheelSpeed(inputPulses/inputEncoder)
# Calculate the distance traveled using the Wheel object's method
traveledDistance = calculateDistance(myWheelSpeed.linearSpeed, timeInterval)

# Display the results in python 2
print("Wheel radius: {} meters".format(myWheel.radius))
print("Wheel diameter: {} meters".format(myWheel.diameter))
print("Wheel circumference: {} meters".format(myWheel.circumference))
print("Wheel Speed: {} RPS".format(myWheelSpeed.revolutionsPerSecond))
print("Wheel Angular Speed: {} Rad/sec".format(myWheelSpeed.angularSpeed))
print("Wheel Linear Speed: {} m/s".format(myWheelSpeed.linearSpeed))
print("Distance traveled with {} pulses: {:.2f} meters".format(inputPulses,traveledDistance))

# Display the results in python 3
#print(f"Wheel radius: {my_wheel.radius} meters")
#print(f"Wheel diameter: {my_wheel.diameter} meters")
#print(f"Wheel circumference: {my_wheel.circumference} meters")
#print(f"Distance traveled with {pulses_received} pulses: {distance_traveled:.2f} meters")