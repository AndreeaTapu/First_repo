# Exercitiul 1:

x = input('Introduceti un string de dimensiune impara ')   # am introdus : avion, dulap
print(x[2])

# Exercitiul 2:

x = input('Introduceti un string de la tastatura ')    # am introdus : caiac
y = x[::-1]
assert x == y, 'Eroare: nu este palindrom'
print('Stringul este palindrom')

# Exercitiul 3:

x = input('Introduceti un string de la tastatura '); cuvant1 = x[0:3]; cuvant2 = x[4:len(x)]; print(cuvant1); print(cuvant2) # am introdus: mar stricat

# Exercitiul 4:

a = input('Introduceti un string de la tastatura ')
primul_caracter_variabila = a[0]
print(primul_caracter_variabila)
ab = a.replace('a', 'A')
abc = ab[1:len(ab)-1]
abc1 = ab[0].lower() + abc + ab[len(ab)-1].lower()
print(abc1)


# Exercitiul 5:

user = input('Introduceti un user ')
password = input('Introduceti o parola ')
lungime = str(len(password))
password1 = password.replace(password, '*' * len(password))

print(f"Parola pentru {user} este {password1} si are {lungime} caractere")
