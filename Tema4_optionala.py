# Exercitiul 1:

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    elif numar % 2 != 0:
        numere_impare.append(numar)

    if numar >= 0:
        numere_pozitive.append(numar)
    elif numar < 0:
        numere_negative.append(numar)
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

# Exercitiul 2:

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
temp = 0
for i in range(0, len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            temp = alte_numere[i]
            alte_numere[i] = alte_numere[j]
            alte_numere[j] = temp
print(alte_numere)

# Exercitiul 3:

import random
numar_secret = random.randint(1, 30)
numar_ghicit = None
print(numar_secret)
while True:
    numar_ghicit_user = int(input("Introduceti un numar "))
    if numar_secret > numar_ghicit_user:
        print("Nr secret e mai mare")
    elif numar_secret < numar_ghicit_user:
        print("Nr secret e mai mic")
    elif numar_secret == numar_ghicit_user:
        print("Felicitari! Ai ghicit!")
        break

# Exercitiul 4:

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

# Exercitiul 5:

tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

for i in range(len(tastatura_telefon)):
  for j in range(len(tastatura_telefon[i])):
    print(f"Cifra curentă este : {tastatura_telefon[i][j]}")
