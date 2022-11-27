# Exercitiul 1:

x = 199535

if len(str(x)) >=4:
    print('x are min 4 cifre')
else:
    print('x nu are min 4 cifre')

# Exercitiul 2:

if len(str(x)) == 6:
    print('x are exact 6 cifre')
else:
    print('x nu are exact 6 cifre')

# Exercitiul 3:

if x % 2 == 0:
    print('x este numar par')
else:
    print("x este numar impar")


# Exercitiul 4:

x = input('Intruduceti numarul ')
y = input('Intruduceti numarul ')
z = input('Intruduceti numarul ')

print(max(x, y, z))

# Exercitiul 5:

x = int(input('Intruduceti numarul '))
y = int(input('Intruduceti numarul '))
z = int(input('Intruduceti numarul '))

sum = x+y+z

if sum == 180:
    print('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')

# Exercitiul 6:

variabila_a = "Coral is either the stupidest animal or the smartest rock"
x = int(input('Introdu un numar '))
print(variabila_a[0:len(variabila_a)-x])

# Exercitiul 7:

variabila_b = variabila_a[0:5] + variabila_a[-5:]
print(variabila_b)

# Exercitiul 8:

variabila_index = variabila_a.index('rock')
print(variabila_index)
print(variabila_a[0:variabila_index])


# Exercitiul 9:

string_tastatura = input(('Introduceti un string '))
assert string_tastatura[0] == string_tastatura[-1], 'Eroare : primul și ultimul caracter nu sunt la fel'
print('Primul și ultimul caracter sunt la fel')

# Exercitiul 10:

string_x = '0123456789'

print(string_x[::2])         # se afiseaza numere pare
print(string_x[1::2])        # se afiseaza numere impare


# Exercitiul bonus:

from random import randint

dice_roll = randint(1, 6)

numar_ghicit_utilizator = int(input('Ghiciti numarul de pe zaruri '))

if numar_ghicit_utilizator < dice_roll:
    print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ghicit_utilizator} si zarul a fost {dice_roll}.")
elif numar_ghicit_utilizator > dice_roll:
    print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ghicit_utilizator} si zarul a fost {dice_roll}.")
elif numar_ghicit_utilizator == dice_roll:
    print(f"Ai ghicit. Felicitari! Ai ales {numar_ghicit_utilizator} si zarul a fost {dice_roll}.")





