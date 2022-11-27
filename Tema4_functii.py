# Exercitiul 1:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for i in range(len(masini)):
    print(f"Masina mea preferata este {masini[i]}")
print('--------FOR--------')

for masina in masini:
    print(f"Masina mea preferata este: {masina}")
print('--------FOR EACH--------')

s = 0
while s in range(len(masini)):
    print(f"Masina mea preferata este: {masini[s]}")
    s += 1
print('--------WHILE--------')

# Exercitiul 2:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for x in masini[1:-1]:
    index = masini.index(x)
    masini[index] = x.upper()
print(masini)

# Exercitiul 3:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masina_dorita_de_cumparator = 'Mercedes'
for i in range(len(masini)):
    print(f"Am gasit masina: {masini[i]}. Mai cautam.")
    if masini[i] == masina_dorita_de_cumparator:
        print("Am gasit masina dorita de dumneavoastra.")
        break

# Exercitiul 4:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Lăstun' or masina == 'Trabant':
                continue
    print(f"S-ar putea să vă placă mașina: {masina}")

# Exercitiul 5:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == 'Lăstun':
        masini_vechi.append(masina)
        masini[masini.index(masina)] = 'Tesla'
    elif masina == 'Trabant':
        masini_vechi.append(masina)
        masini[masini.index(masina)] = 'Tesla'
print(f'Modele noi: {masini}')
print(f'Modele vechi: {masini_vechi}')

# Exercitiul 6:

pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

for key in pret_masini.keys():
    if pret_masini.get(key) < 15000:
        print(f"Pentru un buget de 15000 euro puteti alege masina {key} la pretul de {pret_masini[key]}")

# Exercitiul 7:

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
for numar in numere:
    if numar == 3:
        count += 1
print(f"Numarul 3 apare de {count} ori in lista")

# Exercitiul 8:

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for i in range(len(numere)):
    suma = suma + numere[i]
print(f"Suma numerelor din lista este: {suma}")

# Exercitiul 9:

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = 0
for numar in numere:
    if numar > max:
        max = numar
print(f"Cel mai mare numar din lista este: {max}")

# Exercitiul 10:

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)


