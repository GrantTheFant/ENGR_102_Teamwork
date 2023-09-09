# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Clayton Dodgen (572)
#               Grant Gallun (472)
#               Arman Mediratta (472)
#               Micah Alummoottil (472)
# Section:      472, 572
# Assignment:   THE ASSIGNMENT NUMBER (4.14)
# Date:         9/8/23

#72-16

############ Part A ############
a = input("Enter True or False for a: ")
b = input('Enter True or False for b: ')
c = input("Enter True or False for c: ")




def determinebool(x):
    toReturn = False
    if (x == 't'):
        toReturn = True
    elif(x == 'T'):
        toReturn = True
    elif(x == "True"):
        toReturn = True
    return toReturn

#style comment

############ Part B ############
a = determinebool(a)
b = determinebool(b)

c = determinebool(c)

############ Part C ############
print(f'a and b and c: {bool(int(a & b & c))}')
print(f'a or b or c: {a or b or c}')
print(f'XOR: {not bool(int(a == b))}')
print(f'Odd number: {bool((a+b+c)%2)}')
############ Part D ############
complex_1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
simple_1 = (not b or (not c and not a))
comeplex_2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b
and c) or (a and ((b and not c) or (not b))))
simple_2 = (a or (c and not b))

#s1 = (not a *b) or (not c * b) and (not b) or (not a * b * (not c)) or (a * (not b))
# s2 = (not((b / *)))
#print(a,b,c,)

print("Complex 1:",complex_1)
print("Complex 2:",comeplex_2)
print("Simple 1:",simple_1)
print("Simple 2:", simple_2)

#The amount of times I had to restart parts of the problem and debug my own work has driven me to the brink of insanity. I forgot to put a not that only effects one of 9 outcomes. - Grant


# s1 = (a and not c)
# s2 = ((a and b) or (b and c))