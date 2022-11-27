# def suma_liste_indef(*args):
# 	suma = []
# 	for numar in args:
# 			suma = suma + numar
# 	return suma
#
# def suma_numere_indef(*args):
# 	suma = 0
# 	for numar in args:
# 			suma +=numar
# 	return suma
#
#
# print(suma_numere_indef(1, 4))
# print(suma_numere_indef(1))
# print(suma_numere_indef(1, 11))
#
# print("---------------------------")
#
# lista1 = [1,3,5,7,9]
# lista2 = [0,2,4,6,8]
# print(suma_numere_indef(*lista1))
# print(suma_numere_indef(*lista1,*lista2))
# print(suma_numere_indef(1,3,5,7,9,0,2,4,6,8))
# # print(suma_liste_indef([1,3,5,7,9],[0,2,4,6,8]))
# # suma_numere_indef(1, 3, 5, 7, 9) # trebuie sa se intample
# # suma_numere_indef([1,3,5,7,9]) # nu trebuie sa se intample

from tabulate import tabulate

data = [["Himanshu",1123, 10025], ["Rohit",1126,10029],

             ["Sha",111178,7355.4]]

print(tabulate(data))
print(tabulate(data, headers=["Name","User ID", "Roll. No."]))