# Exercitiul 1:

from calendar import monthrange

def numere_zile_in_luna(an, luna):
    return monthrange(an, luna)[1]

print(numere_zile_in_luna(2022, 8))

# Exercitiul 2:

def functie_calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d

a, b, c, d = functie_calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

# Exercitiul 3:

def frecventa_numarare_lista_de_cifre(lista):
    dictionar_gol = {}
    for i in [1, 1, 2, 2, 2, 5, 6, 8, 9, 5, 8, 7, 7, 0, 6, 9, 9, 8]:
        dictionar_gol[i] = dictionar_gol.get(i, 0) + 1
    return dictionar_gol

if __name__ == "__main__":
    lista = [1, 1, 2, 2, 2, 5, 6, 8, 9, 5, 8, 7, 7, 0, 6, 9, 9, 8]
    print(frecventa_numarare_lista_de_cifre(lista))

# Exercitiul 4:

def maxim_doua_numere( x, y ):
    if x > y:
        return x
    return y
def maxim_trei_numere(x, y, z):
    return maxim_doua_numere(x, maxim_doua_numere(y, z))
print(maxim_trei_numere(7, 21, 13))

# Exercitiul 5:

