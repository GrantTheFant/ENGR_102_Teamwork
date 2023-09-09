# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Clayton Dodgen (572)
#               Grant Gallun (472)
#               Arman Mediratta (472)
#               Micah Alummoottil (472)
# Section:      472, 572
# Assignment:   THE ASSIGNMENT NUMBER (4.13)
# Date:         9/8/23

#72-16


totalPaid = float(input('How much did you pay? '))
totalCost = float(input('How much did it cost? '))
totalChange = totalPaid - totalCost
print(f"You received ${totalChange:.2f} in change. That is...")

quarter = totalChange // 0.25
totalChange = round(totalChange - (quarter * .25), 2)
dime = totalChange // 0.10 
totalChange = round(totalChange - (dime * .1), 2)
nickel = totalChange // 0.05
totalChange = round(totalChange - (nickel * .05), 2)
penny = totalChange / 0.01
totalChange = round(totalChange - (penny * .01), 2)



#print(totalChange)

if quarter > 1:
    print(int(quarter),"quarters")
elif quarter == 1:
    print(int(quarter),'quarter')
if dime > 1:
    print(int(dime),"dimes")
elif dime == 1:
    print(int(dime), 'dime')
if nickel > 1:
    print(int(nickel),"nickels")
elif nickel == 1:
    print(int(nickel), 'nickel')
if penny > 1:
    print(int(penny),"pennies")
elif penny == 1:
    print(int(penny), 'penny')

