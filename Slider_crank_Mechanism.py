import math
import matplotlib.pyplot as plt
import numpy as np



crankLength = float(input("Enter crank Length"))
couplerLength = float(input("Enter coupler Length"))
rpm = float(input("Enter the RPM"))
crankAngle = 0
angVelocity = (2*math.pi*rpm)/60
n = couplerLength / crankLength
crankAngleList = []
pistonVelocityList = []
conrodAngularVelocityList = []
pistonAccelerationList = []
conrodAccelerationList = []

def pistonVelocity(crank,angle,omega,ratio):
    pistonVelocity = crank*omega*(math.sin(math.radians(angle))+(math.sin(math.radians(angle*2)))/(2*ratio))
    return pistonVelocity
def conrodAngularVelocity(omega,angle,ratio):
    conrodAngularVelocity = (omega*math.cos(math.radians(angle)))/math.sqrt((ratio**2)-(math.sin(math.radians(angle))**2))
    return conrodAngularVelocity
def pistonAcceleration(crank,omega,angle,ratio):
    pistonAcceleration = crank*omega**2*(math.cos(math.radians(angle))+(math.cos(math.radians(angle*2)))/ratio)
    return pistonAcceleration
def conrodAcceleration(omega,ratio,angle):
    conrodAcceleration = (-omega**2*math.sin(math.radians(angle))*(ratio**2-1))/(ratio**2-(math.sin(math.radians(angle)))**2)**3/2
    return conrodAcceleration

for i in range(36000):
    crankAngle = i*0.01
    crankAngleList.append(crankAngle)
    pistonVelocityList.append(pistonVelocity(crankLength,crankAngle,angVelocity,n))
    conrodAngularVelocityList.append(conrodAngularVelocity(angVelocity,crankAngle,n))
    pistonAccelerationList.append(pistonAcceleration(crankLength,angVelocity,crankAngle,n))
    conrodAccelerationList.append(conrodAcceleration(angVelocity,n,crankAngle))


#variation of piston velocity with crank angle
print(crankAngleList)
print(pistonVelocityList)
xpoints = np.array(crankAngleList)
y1points = np.array(pistonVelocityList)
plt.plot(xpoints,y1points)
plt.xlabel("Crank Angle")
plt.ylabel("Piston Velocity")
plt.title("Piston Velocity Variation with crank Angle")
plt.show()
plt.close()
#variation of coupler angular velocity with crank angle
print(conrodAngularVelocityList)
y2points = np.array(conrodAngularVelocityList)
plt.plot(xpoints,y2points)
plt.xlabel("Crank Angle")
plt.ylabel("Conrod Angular Velocity")
plt.title("Conrod Angular Velocity Variation with Crank Angle")
plt.show()
#variation of piston acceleration with crank angle
print(pistonAccelerationList)
y3points = np.array(pistonAccelerationList)
plt.plot(xpoints,y3points)
plt.xlabel("Crank Angle")
plt.ylabel("Piston Acceleration")
plt.title("Piston Acceleration Variation with Crank Angle")
plt.show()
#variation of conrod Acceleration with crank angle
print(conrodAccelerationList)
y4points = np.array(conrodAccelerationList)
plt.plot(xpoints,y4points)
plt.xlabel("Crank Angle")
plt.ylabel("Conrod Acceleration")
plt.title("Conrod Acceleration Variation with Crank Angle")
plt.show()
