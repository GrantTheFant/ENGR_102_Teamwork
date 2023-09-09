# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Clayton Dodgen (572)
#               Grant 472
#               Arman 472
#               Micah 472
# Section:      472, 572
# Assignment:   THE ASSIGNMENT NUMBER (Linear Interpolation)
# Date:         8/25/2023
# Team Number:  72-16

#Part 1
import math

time1 = 10
time2 = 55
distance1 = 2027
distance2 = 23027
speed = (distance2 - distance1)/(time2 - time1)


currentTime1 = 25

currentPos1 = (speed * currentTime1) + (2027 - speed * 10) #Expanded Equation
print('Part 1:\nFor t =', currentTime1, 'minutes, the position p =', currentPos1,"kilometers")

#Part 2

currentTime2 = 300
currentPos2 = (speed * currentTime2) + (2027 - speed * 10) #Expanded Equation
radius = 6745
distance3 = 23027
circumference = radius * math.pi * 2

print('Part 2:\nFor t =', currentTime2, 'minutes, the position p =', (currentPos2 % circumference))
