# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Clayton Dodgen (572)
#               Grant 472
#               Arman 472
#               Micah Alummoottil 472
# Section:      472, 572
# Assignment:   3.15 (Unit Conversions)
# Date:         8/31/2023
# Team Number:  72-16
import math
conv = float(input("Please enter the quantity to be converted: "))
print()
#definitions command is same for all, just change multiplication 
def pounds_newtons(conversion):
    newtons = 4.448222 * conversion
    return newtons
print (f'{conv:.2f}', "pounds force is equivalent to", f'{pounds_newtons(conv):.2f}', "Newtons")
def meters_feet(conversion):
    feet = 3.28084 * conversion
    return feet
print (f'{conv:.2f}', "meters is equivalent to", f'{meters_feet(conv):.2f}', "feet")
def atmospheres_kilo(conversion):
    kilo = 101.325 * conversion
    return kilo
print (f'{conv:.2f}', "atmospheres is equivalent to", f'{atmospheres_kilo(conv):.2f}', "kilopascals")
def watts_btu(conversion):
    btu = 3.412141633 * conversion
    return btu
print (f'{conv:.2f}', "watts is equivalent to", f'{watts_btu(conv):.2f}', "BTU per hour")
def liters_gallons(conversion):
    gallons = 15.850323141489 * conversion
    return gallons
print (f'{conv:.2f}', "liters per second is equivalent to", f'{liters_gallons(conv):.2f}', "US gallons per minute")
def celc_fah(conversion):
    fah = (9/5 * conversion) + 32
    return fah
print (f'{conv:.2f}', "degrees Celsius is equivalent to", f'{celc_fah(conv):.2f}', "degrees Fahrenheit")
