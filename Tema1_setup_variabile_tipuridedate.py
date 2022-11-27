# Exercitiul 1:
# O variabila este o locatie din memoria computerului folosita pentru a stoca informatii

# Exercitiul 2:
# declarare si initializare variabile

nume = 'Tapu'
varsta = 27
ore_pentru_invatat = 2.5
invat_python = True

#  Exercitiul 3:
# folosirea functiei (type)

print(type(nume))
print(type(varsta))
print(type(ore_pentru_invatat))
print(type(invat_python))

#  Exercitiul 4:
# functia round si suprascriere

ore_pentru_invatat=round(ore_pentru_invatat)
print(ore_pentru_invatat)
print(type(ore_pentru_invatat))

#  Exercitiul 5:

print(f'Numele meu de familie este {nume}')
print(f'Varsta mea este de {varsta}')
print(f'Eu invat python {ore_pentru_invatat} h/pe zi')
print(invat_python)

#  Exercitiul 6:

nume = input('Introduceti numele ')
prenume= input('Introduceti prenumele ')
caractere = len(nume) + len(prenume)
print(f'Numele complet are {caractere} caractere')

# Exercitiul 7:

lungime = int(input('Introduceti lungimea '))
latime = int(input('Introduceti latimea '))
print(f"Aria triunghiului este ",  lungime * latime)

#  Exercitiul 8:

variabila_string = 'Coral is either the stupidest animal or the smartest rock'
print(variabila_string.count('the'))

#  Exercitiul 9:

a = variabila_string.replace('the','THE')
print(a)

#  Exercitiul 10:

assert variabila_string.isnumeric() == True, 'Eroare, nu contine numere'
print('Acest string contine numere')







