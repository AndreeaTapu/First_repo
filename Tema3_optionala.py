# Exercitiul optional

jucatori = ['Mihai', 'Ion', 'Andrei', 'Dan', 'David']









jucatori = ['Mihai', 'Ion', 'Andrei', 'Dan', 'David']
print(jucatori)
schimbari_max = 3
schimbari_efectuate = 0

jucatori_scosi = ['Ion']

if 'Ion' in jucatori and schimbari_efectuate <= 3:
    jucatori.pop(1)
    print(f'A iesit {jucatori_scosi[0]}')
    jucatori.insert(1, 'Alexandru')
    print(f'A intrat {jucatori[1]}')
schimbari_efectuate += 1



print(jucatori)


# if 'Dan' in jucatori and schimbari_efectuate <= 3:
#     jucatori.pop(3)
#     print(f'A iesit {jucatori_scosi[1]}')
#     jucatori.insert(3, 'Petru')
#     print(f'A intrat {jucatori[3]}')
# schimbari_efectuate += 1
# print('Mai ai', schimbari_max-schimbari_efectuate, 'schimbari')
#
# print(jucatori)



