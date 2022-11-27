# Exercitiul 1:

# if else = evalueaza conditii si bifurca codul in functie de rezultat

# Exercitiul 2:

x = int(input('Introduceti numarul'))
if x >=0:
    print('numar natural')
else:
    print('nu este numar natural')

# Exercitiul 3:

x = int(input('Introduceti numarul'))
if x > 0:
    print('numar pozitiv')
elif x == 0:
    print('numar neutru')
elif x < 0:
    print('numar negativ')

# Exercitiul 4:

x = 5
if x >= -2 and x <= 13:
    print('x este in acest interval')
else:
    print('x nu este in acest interval')

# Exercitiul 5:

x = 7
y = 5
if (x - y) < 5:
    print('se indeplineste conditia')
else:
    print('nu se indeplineste conditia')

x = 200
y = 150
if (x % y) < 5:
    print('se indeplineste conditia')
else:
    print('nu se indeplineste conditia')

# Exercitiul 6:

x = 2
if not x >= 5 and x <= 27:
    print('x este in acest interval')
else:
    print('x nu este in acest interval')

# Exercitiul 7:

x = 8
y = 12

if x == y:
    print('sunt egale')
elif x > y:
    print('x este mai mare decat y')
else:
    print('y este mai mare decat x')


# Exercitiul 8:

x = int(input('Introduceti numarul '))
y = int(input('Introduceti numarul '))
z = int(input('Introduceti numarul '))

if x == y != z or x!= y == z or y!= x == z:
    print('triunghiul este isoscel')
elif x == y and x == z and y == z:
    print('triungiul este echilateral')
elif x != y != z:
    print('triunghi oarecare')


# Exercitiul 9:

x = input('Scrie o litera de la tastatura ')
vocale = 'a', 'e', 'i', 'o', 'u'
if x in vocale:
    print("Este vocala")
else:
    print("Este Consoana")

# Exercitiul 10:

note = int(input('Introduceti nota'))
if note <= 4:
    print('f')
elif note > 4 and note <= 6:
    print('e')
elif note > 6 and note <= 7:
    print('d')
elif note > 7 and note <= 8:
    print('c')
elif note > 8 and note <= 9:
    print('b')
elif note > 9 and note <= 10:
    print('a')
else:
    print('numar mai mare de 10')




