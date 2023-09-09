# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Clayton Dodgen (572)
#               Grant Gallun (472)
#               Arman Mediratta (472)
#               Micah Alummoottil (472)
# Section:      472, 572
# Assignment:   THE ASSIGNMENT NUMBER (3.16)
# Date:         9/4/23

#72-16
import math

time1 = float(input('Enter time 1: '))
distancex1 = float(input('Enter the x position of the object at time 1: '))
distancey1 = float(input('Enter the y position of the object at time 1: '))
distancez1 = float(input('Enter the z position of the object at time 1: '))

time2 = float(input('Enter time 2: '))
distancex2 = float(input('Enter the x position of the object at time 2: '))
distancey2 = float(input('Enter the y position of the object at time 2: '))
distancez2 = float(input('Enter the z position of the object at time 2: '))
speedx = (distancex2 - distancex1)/(time2 - time1)
speedy = (distancey2 - distancey1)/(time2 - time1)
speedz = (distancez2 - distancez1)/(time2 - time1)
counter=1

def interpolate(desiredtime):
 distancex = (desiredtime-time1)*speedx+distancex1#(distancex1-speedx*time1)+speedx*desiredtime
 distancey = (desiredtime-time1)*speedy+distancey1
 distancez = (desiredtime-time1)*speedz+distancez1
 print("At time", f"{desiredtime:.2f} seconds the object is at ({distancex:.3f}, {distancey:.3f}, {distancez:.3f})")

print()

def runInter(t1, t2):
    interval = (t2 - t1)/4
    interpolate(t1)
    t1 += interval
    interpolate(t1)
    t1 += interval
    interpolate(t1)
    t1 += interval
    interpolate(t1)
    interpolate(t2)
    
#run the print statements with incrementer

runInter(time1, time2)
#hehe

