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

def computeOdometry(index2Updte, rotData, velocityData):
    previousPose = np.array([
        [poseEstimation.x[index2Updte-1]],
        [poseEstimation.y[index2Updte-1]],
        [poseEstimation.yaw[index2Updte-1]]
    ])
    velocititesFactor = samplingRate * np.dot(rotData, velocityData)
    poseEstimation.x[index2Updte] = previousPose[0] + velocititesFactor[0]
    poseEstimation.y[index2Updte] = previousPose[1] + velocititesFactor[1]
    poseEstimation.yaw[index2Updte] = previousPose[2] + velocititesFactor[2]

def vehicleParameters(pulsesPerSecond, pulsesPerRevolution, wheelRadius, widthValue):
    angularSpeed = 2 * np.pi * pulsesPerSecond / pulsesPerRevolution
    linearSpeed = angularSpeed * wheelRadius
    localXSpeed = linearSpeed
    localTurninigSpeed = angularSpeed * widthValue / 2
    myRobot.update(localXSpeed, 0, localTurninigSpeed)
    localRobotSpeed = np.array([
        [myRobot.xSpeed],
        [myRobot.ySpeed],
        [myRobot.turningVel]
    ])
    return localRobotSpeed, angularSpeed, linearSpeed

def rotateAroundZ(previousYaw):
    cosResult = np.cos(previousYaw)
    sinResult = np.sin(previousYaw)
    rotZ = np.array([
        [cosResult, -sinResult, 0],
        [sinResult, cosResult, 0],
        [0, 0, 1]
    ])
    return rotZ

encoderPulsesPerRevolution = int(input("Enter quantity of Encoder Pulses per Revolution: "))
pulsesPerSecond = int(input("Enter quantity of Pulses per Second: "))
WHEELRADIUS = float(input("Enter Wheel Radius (m): "))
WIDTHCONTACTPOINT = float(input("Enter Vehicle Width (W - m): "))
initialX = float(input("Enter Starting X position: "))
initialY = float(input("Enter Starting Y position: "))
initialYaw = float(input("Enter Starting Heading Value (degrees): "))
elapsedTime = int(input("Enter elapsed time (seconds): "))

myRobot = Robot(0.0, 0.0, 0.0)

samplingRate = 0.25
vectorSize = elapsedTime / samplingRate
poseEstimation = Pose(int(vectorSize))

currentIndex = 0
angleRadians = np.radians(initialYaw)
poseEstimation.x[currentIndex] = initialX
poseEstimation.y[currentIndex] = initialY
poseEstimation.yaw[currentIndex] = angleRadians

for currentIndex in range(1, int(vectorSize)):
    rotZMat = rotateAroundZ(poseEstimation.yaw[currentIndex-1])
    robotSpeedData, angularSpeed, linearSpeed = vehicleParameters(pulsesPerSecond, encoderPulsesPerRevolution, WHEELRADIUS, WIDTHCONTACTPOINT)
    computeOdometry(currentIndex, rotZMat, robotSpeedData)

print("\nFinal Pose Values: ")
print("Xg: ", poseEstimation.x[-1])
print("Yg: ", poseEstimation.y[-1])
print("Og (radians): ", poseEstimation.yaw[-1])
print("\nWheel Speeds: ")
print("Angular Speed per Wheel (rad/s): ", angularSpeed)
print("Linear Speed per Wheel (m/s): ", linearSpeed)