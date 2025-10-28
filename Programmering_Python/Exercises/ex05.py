# uppgift 1a
inp = input('Skriv ett ord: ')
print(f'Ditt ord har {len(inp)} bokstäver.')
# uppgift 1b
versal = 0
gemen = 0
for bokstav in inp:
    if bokstav.isupper():
        versal += 1
    elif bokstav.islower():
        gemen += 1
print(f'{versal} var versaler och {gemen} var gemener.')

# uppgift 2
citat = 'A picture says more than a thousand words, a mathematical formula says more than a thousand pictures.'
print(f'Citatet har {len(citat.split())} ord.')

# uppgift 3
inp = input('Skriv en sekvens av bokstäver så ska vi se ifall det är en palindrom: ').lower().replace(' ', '')
pni = inp[::-1]
if inp == pni:
    print('Det var en palindrom.')
else:
    print('Det var inte en palindrom.')

# uppgift 4
string = 'Pure mathermatics is, in its way, the poetry of logical ideas'
vokaler = ['a', 'e', 'i', 'o', 'u', 'y']
konsonanter = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
vcount = 0
kcount = 0
tcount = 0
for bokstav in string.lower().replace(' ', ''):
    if bokstav in vokaler:
        vcount += 1
    elif bokstav in konsonanter:
        kcount += 1
    else:
        tcount += 1
print(f'I texten "{string}" är det {vcount} vokaler, {kcount} konsonanter och {tcount} tecken exkl. mellanslag.')

# uppgift 5a
meddelande = input('Skriv ett meddelande för kryptering: ')
alfabetet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
krypterat = []
for bokstav in meddelande:
    if bokstav.isupper():
        bokstav = bokstav.lower()
        currentind = alfabetet.index(bokstav)
        nextind = (currentind + 1) % len(alfabetet)
        krypterat.append(alfabetet[nextind].upper())
    elif bokstav in alfabetet:
        currentind = alfabetet.index(bokstav)
        nextind = (currentind + 1) % len(alfabetet)
        krypterat.append(alfabetet[nextind])
    else:
        krypterat.append(bokstav)
krypterat = ''.join(krypterat)
print(krypterat)
# uppgift 5b
dekrypterat = []
for bokstav in krypterat:
    if bokstav.isupper():
        bokstav = bokstav.lower()
        currentind = alfabetet.index(bokstav)
        nextind = currentind - 1
        dekrypterat.append(alfabetet[nextind].upper())
    elif bokstav in alfabetet:
        currentind = alfabetet.index(bokstav)
        nextind = currentind - 1
        dekrypterat.append(alfabetet[nextind])
    else:
        dekrypterat.append(bokstav)
dekrypterat = ''.join(dekrypterat)
print(dekrypterat)
# uppgift 5c
val = int(input('Välj 1 för att kryptera ett meddelande eller välj 2 för att dekryptera ett meddelande: '))
if val == 1:
    meddelande = input('Skriv ett meddelande för kryptering: ')
    krypterat = []
    for bokstav in meddelande:
        if bokstav.isupper():
            bokstav = bokstav.lower()
            currentind = alfabetet.index(bokstav)
            nextind = (currentind + 1) % len(alfabetet)
            krypterat.append(alfabetet[nextind].upper())
        elif bokstav in alfabetet:
            currentind = alfabetet.index(bokstav)
            nextind = (currentind + 1) % len(alfabetet)
            krypterat.append(alfabetet[nextind])
        else:
            krypterat.append(bokstav)
    krypterat = ''.join(krypterat)
    print(f'Ditt meddelande efter kryptering: {krypterat}')
elif val == 2:
    meddelande = input('Fyll i ditt krypterade meddelande för dekryptering: ')
    dekrypterat = []
    for bokstav in meddelande:
        if bokstav.isupper():
            bokstav = bokstav.lower()
            currentind = alfabetet.index(bokstav)
            nextind = currentind - 1
            dekrypterat.append(alfabetet[nextind].upper())
        elif bokstav in alfabetet:
            currentind = alfabetet.index(bokstav)
            nextind = currentind - 1
            dekrypterat.append(alfabetet[nextind])
        else:
            dekrypterat.append(bokstav)
    dekrypterat = ''.join(dekrypterat)
    print(f'Ditt meddelande efter dekryptering: {dekrypterat}')
else:
    print('Du valde varken 1 eller 2 och får därmed göra varken eller.')