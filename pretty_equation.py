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
a = int(input('Please enter the coefficient A: '))
b = int(input('Please enter the coefficient B: '))
c = int(input('Please enter the coefficient C: '))

print('The quadratic equation is', end=' ')
#a
if a == 1:
    print('x^2', end=' ')
elif a == -1:
    print('- x^2', end=' ')
elif a == 0:
    print('', end='')
elif a < -1:
    print(f'- {abs(a)}x^2', end=' ')
else:
    print(f'{a}x^2', end=' ')

#style comment lol
if (b == 1 and a != 0):
    print('+ x', end=' ')
elif(b == 1 and a == 0):
    print("x", end=(" "))
elif b == -1:
    print('- x', end=' ')
elif b == 0:
    print('', end='')
elif b < -1:
    print(f'- {abs(b)}x', end=' ')
elif (b > 1 and a != 0):
    print(f'+ {b}x', end=' ')
else:
    print(f'{b}x', end=(" "))


if c == 1:
    print(f'+ {c}', end= ' = 0\n')
elif c == -1:
    print(f'- {abs(c)}', end=' = 0\n"')
elif c > 1:
    print(f"+ {c}", end=" = 0\n")
elif c < 0:
    print(f'- {abs(c)}', end= ' = 0\n')
elif c == 0:
    print('', end='= 0\n')

