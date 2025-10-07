# uppgift 1
AIM25G = {
    'Introduktionskurs till AI': 5,
    'Programmering med Python': 40,
    'Databehandling': 25,
    'Linjär algebra': 20,
    'Statistiska metoder': 30,
    'Maskininlärning': 45,
    'Databaser': 25,
    'Data Engineering och agila metoder': 45,
    'LIA 1': 40,
    'Djup Maskininlärning': 40,
    'LIA 2': 70,
    'Examensarbete': 15
}
yhp = sum(AIM25G.values())

# uppgift 2
import random as rd
slagsort = {i: 0 for i in range(1, 7)}
def slå_tärning(slag):
    for x in range(slag):
        dr = rd.randint(1, 6)
        slagsort[dr] += 1
    return
slå_tärning(1000000)
print(slagsort)

# uppgift 3
with open('pokemon_list.txt', 'r', encoding='utf-8') as pokemon_list:
    pokemon_list.seek(0)
    list = pokemon_list.readlines()
    listan = [line.split() for line in list]
    pokedex = {

    }
    for rad in listan:
        pokedex[rad[1]] = f'Typ: {rad[2]}, id#: {rad[0]}'

# uppgift 4
with open('morse.txt','r', encoding='utf-8') as morse:
    list = morse.readlines()
    listan = [line.replace(':', '').split() for line in list]
    morselexikon = {rad[0]: rad[1] for rad in listan}
    def skriv_morse(översätt):
        print(f'"{översätt}" översatt till morse är: ')
        for x in översätt:
            print(morselexikon[x] if x in morselexikon else ' ', end=' ')
        print('\nDisclaimer: Endast bokstäver kan översättas, siffror och specialtecken ersätts av mellanslag.')
    översätt = input('Skriv ett ord eller en mening du vill få översatt till morse: ').upper()
    skriv_morse(översätt)