import time
# Universal standar to work with numerical data in Python
import numpy as np

# Pose class contains three arrays that will store vehicle position and orientation values
class Pose:
    def __init__(self, size):
        self.x = np.zeros(size)
        self.y = np.zeros(size)
        self.yaw = np.zeros(size)
    def update(self, newX, newY, newYaw):
        self.x = newX
        self.y = newY
        self.yaw = newYaw
# Robot class stores vehicle variables from its local frame: left and right speed & orientation
class Robot:
    def __init__(self, xSpeed,ySpeed,turningVel):
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.turningVel = turningVel
    def update(self, newXSpeed, newYSpeed, newTurnSpeed):
        self.xSpeed = newXSpeed
        self.ySpeed = newYSpeed
        self.turningVel = newTurnSpeed

# This function contains the equation of the forward kinematic model for a differential drive vehicle
def computeOdometry(index2Updte, rotData, velocityData):
    # GET PREVIOUS POSE DATA FROM THE POSE VECTOR
    previousPose = np.array([
        [poseEstimation.x[index2Updte-1]],
        [poseEstimation.y[index2Updte-1]],
        [poseEstimation.yaw[index2Updte-1]]
    ])
    # SAVE THE CURRENT POSE DATA INTO THE POSE STRUCTURE
    velocititesFactor = samplingRate*np.dot(rotData,velocityData)
    poseEstimation.x[index2Updte] = previousPose[0] + velocititesFactor[0]
    poseEstimation.y[index2Updte] = previousPose[1] + velocititesFactor[1]
    poseEstimation.yaw[index2Updte] = previousPose[2] + velocititesFactor[2]
    
    
# Compute current vehicle speed and orientation variables
def vehicleParameters(rightWheelSpeed, leftWheelSpeed, wheelRadius, widthValue):
    localXSpeed = (wheelRadius*rightWheelSpeed/2)+(wheelRadius*leftWheelSpeed/2)
    localTurninigSpeed = (wheelRadius*rightWheelSpeed/(2*widthValue))-(wheelRadius*leftWheelSpeed/(2*widthValue))
    myRobot.update(localXSpeed, 0, localTurninigSpeed)
    localRobotSpeed = np.array([
        [myRobot.xSpeed],
        [myRobot.ySpeed],
        [myRobot.turningVel]
    ])
    return localRobotSpeed

# Compute the new rotational matrix 
# Make sure the argument previousYaw is in radians 
def rotateAroundZ(previousYaw):
    cosResult = np.cos(previousYaw)
    sinResult = np.sin(previousYaw)
    rotZ = np.array([
        [cosResult, -sinResult, 0],
        [sinResult, cosResult, 0],
        [0, 0, 1]
    ])#START ODOMETRY COMPUTATION
    return rotZ


# ==== USER INPUTS
rightSpeed = float(input("Enter Starting Speed of Right Wheel: "))
leftSpeed = float(input("Enter Starting Speed of Left Wheel: "))
initialX = float(input("Enter Starting X position: "))
initialY = float(input("Enter Starting Y position: "))
initialYaw = float(input("Enter Starting Heading Value -degrees-: "))

# ==== Physical Parameters of the Differential Mobile Robot SETUP ====
WHEELRADIUS = 0.076/2.0 # in mts
WIDTHCONTACTPOINT = 0.22 # in mts
myRobot = Robot(0.0,0.0,0.0)

# ==== TIME REQUIREMENTS SETUP ====
# Setup elapsed time and sampling-rate for the test
elapsedTime = 5
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
#    print("Pass time: ", pastTime)
#    print("Count: ", currentIndex)
#    print("Delta Time: ", time.time()-pastTime)
    currentTime = time.time()
    if (currentTime-pastTime) >= samplingRate:
        
        rotZMat = rotateAroundZ(poseEstimation.yaw[currentIndex-1])
        robotSpeedData = vehicleParameters(rightSpeed,leftSpeed,WHEELRADIUS, WIDTHCONTACTPOINT)
        computeOdometry(currentIndex, rotZMat, robotSpeedData)
        pastTime = currentTime
        currentIndex += 1
        print("Count: ", currentIndex)
    
# === LATELY, DISPLAY SAMPLED POSES ====
# Print final pose values
print("Pose Values: ")
print("x: ", poseEstimation.x)
print("y: ", poseEstimation.y)
print("yaw: ", poseEstimation.yaw)