import time
import numpy as np

class Pose:
    def __init__(self, size):
        self.x = np.zeros(size)
        self.y = np.zeros(size)
        self.yaw = np.zeros(size)
    def update(self, newX, newY, newYaw):
        self.x = newX
        self.y = newY
        self.yaw = newYaw

class Robot:
    def __init__(self, xSpeed, ySpeed, turningVel):
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.turningVel = turningVel
    def update(self, newXSpeed, newYSpeed, newTurnSpeed):
        self.xSpeed = newXSpeed
        self.ySpeed = newYSpeed
        self.turningVel = newTurnSpeed

def computeOdometry(index2Updte, rotData, velocityData, delta_t, L, delta_theta):
    previousPose = np.array([
        [poseEstimation.x[index2Updte-1]],
        [poseEstimation.y[index2Updte-1]],
        [poseEstimation.yaw[index2Updte-1]]
    ])
    velocititesFactor = delta_t * np.dot(rotData, velocityData)
    poseEstimation.x[index2Updte] = previousPose[0] + velocititesFactor[0]
    poseEstimation.y[index2Updte] = previousPose[1] + velocititesFactor[1]
    poseEstimation.yaw[index2Updte] = previousPose[2] + (velocititesFactor[0] * np.tan(delta_theta)) / L

def vehicleParameters(encoder_pulses, pulses_per_second, wheel_radius, delta_theta, L):
    V = (2 * np.pi * wheel_radius * pulses_per_second) / encoder_pulses
    localXSpeed = V * np.cos(delta_theta)
    localYSpeed = V * np.sin(delta_theta)
    localTurninigSpeed = V * np.tan(delta_theta) / L
    myRobot.update(localXSpeed, localYSpeed, localTurninigSpeed)
    localRobotSpeed = np.array([
        [myRobot.xSpeed],
        [myRobot.ySpeed],
        [myRobot.turningVel]
    ])
    return localRobotSpeed

def rotateAroundZ(previousYaw):
    cosResult = np.cos(previousYaw)
    sinResult = np.sin(previousYaw)
    rotZ = np.array([
        [cosResult, -sinResult, 0],
        [sinResult, cosResult, 0],
        [0, 0, 1]
    ])
    return rotZ

# ==== USER INPUTS
encoder_pulses = 20
pulses_per_second = 80
wheel_radius = 0.036
delta_theta = np.radians(0)  # converting degrees to radians
L = 0.22  # WheelBase (lb+lf) in meters
initialX = 0.0
initialY = 0.0
initialYaw = 0.0

# ==== Physical Parameters of the Differential Mobile Robot SETUP ====
WHEELRADIUS = 0.076/2.0 # in mts
WIDTHCONTACTPOINT = 0.22 # in mts
myRobot = Robot(0.0,0.0,0.0)

# ==== TIME REQUIREMENTS SETUP ====
# Setup elapsed time and sampling-rate for the test
elapsedTime = 2
samplingRate = 0.25
# ==== POSE VECTOR SIZE CALCULATION === 
vectorSize = elapsedTime/samplingRate
poseEstimation = Pose(int(vectorSize))
# ==== INITIAL POSE VALUES GOES TO 1st VALUE IN POSE VECTOR ====
# Variable of control to store into the Pose vector positions
currentIndex = 0
# Define a 3x3 Z-axis rotational matrix
angleRadians = np.radians(initialYaw)
# Starting pose vector values setup
poseEstimation.x[currentIndex] = initialX
poseEstimation.y[currentIndex] = initialY
poseEstimation.yaw[currentIndex] = angleRadians

# ==== DELTA-TIME REQUIREMTENS SETUP ====
# The algoritm is about to star so it nees to record past and curren time variables.
# Compute the finishing time for the test.
endTime = time.time() + elapsedTime # time.time() returns time values in seconds
# Initial past time
pastTime = (endTime - elapsedTime)

# === START ODOMETRY COMPUTATION ====
# As long as current time is less than endTime
while time.time() <= endTime:
    currentTime = time.time()
    if (currentTime-pastTime) >= samplingRate:
        rotZMat = rotateAroundZ(poseEstimation.yaw[currentIndex])
        robotSpeedData = vehicleParameters(encoder_pulses, pulses_per_second, wheel_radius, delta_theta, L)
        computeOdometry(currentIndex, rotZMat, robotSpeedData, samplingRate, L, delta_theta)
        pastTime = currentTime
        currentIndex += 1
        print("Count: ", currentIndex)
        # Check if we have reached the end of our pose arrays
        if currentIndex >= len(poseEstimation.x):
            break

# === LATELY, DISPLAY SAMPLED POSES ====
# Print final pose values
print("Pose Values: ")
print("x: ", poseEstimation.x)
print("y: ", poseEstimation.y)
print("yaw: ", poseEstimation.yaw)
