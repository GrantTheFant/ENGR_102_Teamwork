# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brooks Dodgen
#               Grant Gallun
#               Arman Mediratta
#               Micah Alummoottil
# Section:      472
# Assignment:   6.11.1: LAB: Pyramid area (part 1)
# Date:         21 9 2023

#72-16
from math import *

num_meters = float(input('Enter the side length in meters: '))
print('')
num_layers = int(input('Enter the number of layers: '))
print('')

def triangle_area(sidelength):

    height_triangle=sqrt(pow(sidelength,2)-pow(.5*sidelength,2))
    area_triangle=.5*height_triangle*sidelength
    return(area_triangle)


lowest = triangle_area((num_meters*num_layers))
surface_areaside = 0
for i in range(num_layers+1):
    surface_areaside += num_meters * num_meters * 3 * i
totalsurface = surface_areaside + lowest
        

print(f'You need {totalsurface:.2f} m^2 of gold foil to cover the pyramid')