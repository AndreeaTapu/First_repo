# Exercitiul 1:

def suma_doua_numere(nr_1, nr_2):
    suma = nr_1 + nr_2
    print(f"Suma celor doua numere este: {suma}")

suma_doua_numere(15, 56)

# Exercitiul 2:

x = int(input('Introduceti un numar '))

def numar_par_sau_numar_impar(x):

    if x % 2 == 0:
        print(x, "Numarul este par")
    else:
        print(x, "Numarul este impar")

numar_par_sau_numar_impar(x)

# Exercitiul 3:

def len_nume_prenume(nume, prenume):
    return len(nume + prenume)

print(len_nume_prenume('Tapu', 'Andreea'))

# Exercitiul 4:

def aria_triunghiului (latime, inaltime):
    aria = latime * inaltime
    print(f"Aria dreptunghiului este: {aria} ")
latime = int(input("Introduceti latimea "))
inaltime = int(input("Introduceti inaltimea "))
aria_triunghiului(latime, inaltime)

# Exercitiul 5:

import math

def aria_cercului (raza):
    aria_c = raza**2*math.pi
    return aria_c

raza = int(input("Introduceti raza cercului "))
print("Aria cercului este:", aria_cercului(raza))

# Exercitiul 6:

def caracter_intr_un_string_dat ():
    string_de_verificat = "Andreea Tapu"
    if caracter_introdus in string_de_verificat:
        return True
    else:
        return False

caracter_introdus = input("Introduceti un caracter ")
print(caracter_intr_un_string_dat())

# Exercitiul 7:

def caractere_lower_upper(string_caractere):
    caractere_lower = 0
    caractere_upper = 0
    for caracter in string_caractere:
        if caracter.islower():
            caractere_lower = caractere_lower + 1
        elif caracter.isupper():
            caractere_upper = caractere_upper + 1
    print(f'Numarul de caractere lower: {caractere_lower}')
    print(f'Numarul de caractere upper: {caractere_upper}')


caractere_lower_upper("abcDEFmnoFVis")

# Exercitiul 8:

def creare_lista():
    n = int(input("Introduceti numerele = "))
    lista_numere_pozitive = []
    for i in range(n):
        elem = int(input("Elementul " + str(i) + " este: "))
        if elem > 0:
            lista_numere_pozitive.append(elem)
    return lista_numere_pozitive

print(f"Lista numerelor pozitive este :{creare_lista()}")

# Exercitiul 9:

def numere_de_comparat(nr_1, nr_2):
    if nr_1 > nr_2:
        print(f"Primul numar {nr_1} este mai mare decat al doilea numar {nr_2}")
    elif nr_1 < nr_2:
        print(f"Al doilea numar {nr_2} este mai mare decat primul numar {nr_1}")
    elif nr_1 == nr_2:
        print("Numerele sunt egale")

numere_de_comparat(15, 15)

# Exercitiul 10:

def numar_set_numere(nr, set):
    if nr in set:
        print(f"Nu am adaugat numărul {nr} în set. Acesta există deja")
        return False
    else:
        set.add(nr)
        print(f"Am adaugat numărul nou {nr} în set’")
        return True

set = {7, 0, 2, -6, 8, 5, 1}
numar_set_numere(2, set)
















