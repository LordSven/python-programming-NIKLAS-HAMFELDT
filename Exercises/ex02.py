# uppgift 1
print('1)', end=' ')
nummer = -10
while nummer <= 10:
    print(nummer, end=' ')
    nummer += 1
print() # endast för att nästa uppgift ska börja på sin egen newline

# uppgift 2
nummer1 = 0
summa1 = 0
print('2a)', end=' ')
while nummer1 <= 98:
    nummer1 += 1
    summa1 += nummer1
    print(nummer1, '+', end=' ')
    if nummer1 == 99:
        nummer1 += 1
        summa1 += nummer1
        print(nummer1, f'= {summa1}')
nummer2 = -1
summa2 = 0
print('2b)', end=' ')
while nummer2 <= 96:
    nummer2 += 2
    summa2 += nummer2
    print(nummer2, '+', end=' ')
    if nummer2 == 97:
        nummer2 += 2
        summa2 += nummer2
        print(nummer2, f'= {summa2}')

# uppgift 3
import random
print('3a)',end=' ')
gissningar = 0
rnummer = random.randint(1, 100)
gissning = int(input('Du har fem försök på dig att gissa på en siffra från 1 - 100: '))
while gissningar < 4:
    gissningar += 1
    if gissning > rnummer:
        gissning = int(input(f'{gissning} var för högt, du har {5 - gissningar} försök kvar: '))
    elif gissning < rnummer:
        gissning = int(input(f'{gissning} var för lågt, du har {5 - gissningar} försök kvar: '))
    else:
        break
if gissning == rnummer:
    print('Du gissade rätt!')
else:
    print(f'Tyvärr, din sista gissning var {gissning} och rätt svar var {rnummer}.')
print('3b)', 'Nu ska vi se om datorn kan gissa bättre än vad du gjorde: ')
gissningar = 0
rnummer = random.randint(1, 100)
låg = 1
hög = 100
while gissningar < 5:
    gissning = (låg + hög) // 2
    gissningar += 1
    if gissning > rnummer:
        print(f'Datorn gissade {gissning} och det var för högt.')
        hög = gissning - 1
    elif gissning < rnummer:
        print(f'Datorn gissade {gissning} och det var för lågt.')
        låg = gissning + 1
    else:
        break
if gissning == rnummer:
    print(f'Datorn gissade rätt, siffran var {rnummer}!')
else:
    print(f'Datorn var inte bättre än vad du var.')

# uppgift 4a
rgissningar = 0
svar = input('Vill du spela ett spel? ')
ja = 'Tryck y för ja'
nej = 'Tryck n för nej'
while svar == 'y':
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    print(f'Vad blir {x} * {y}?')
    gissning = input()
    if int(gissning) == x * y:
        print('Bra jobbat!')
        rgissningar += 1
        print(f'{ja}\n{nej}')
        svar = input('Vill du spela igen? ')         
    elif int(gissning) != x * y:
        print(f'Du svarade {gissning} men rätt svar var {x * y}.')
        print(f'{ja}\n{nej}')
        svar = input('Vill du spela igen? ')
    elif svar == 'n':
        break
    else:
        print('Du måste välja y eller n ')
print(f'Tack för att du spelade, du svarade rätt {rgissningar} gånger')
# uppgift 4b/c
rgissningar = 0
svar = input('Vill du spela ett spel? ')
while svar == 'ja' or svar == 'Ja' or svar == 'jo' or svar == 'Jo':
    svar = input('Välj svårighetsgrad 1 för Lätt, 2 för Medel eller 3 för Svår ')
    if svar == '1':
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        print(f'Vad blir {x} * {y}?')
        svar = input()
        if int(svar) == x * y:
            print('Bra jobbat!')
            rgissningar += 1
            svar = input('Vill du spela igen? ')         
        elif int(svar) != x * y:
            print(f'Du svarade {svar} men rätt svar var {x * y}.')
            svar = input('Vill du spela igen? ')
        elif svar == 'stopp':
            break
    elif svar == '2':
        x = random.randint(5, 20)
        y = random.randint(5, 20)
        print(f'Vad blir {x} * {y}?')
        svar = input()
        if int(svar) == x * y:
            print('Bra jobbat!')
            rgissningar += 1
            svar = input('Vill du spela igen? ')         
        elif int(svar) != x * y:
            print(f'Du svarade {svar} men rätt svar var {x * y}.')
            svar = input('Vill du spela igen? ')
        elif svar == 'stopp':
            break
    elif svar == '3':
        x = random.randint(15, 40)
        y = random.randint(15, 40)
        print(f'Vad blir {x} * {y}?')
        svar = input()
        if int(svar) == x * y:
            print('Bra jobbat!')
            rgissningar += 1
            svar = input('Vill du spela igen? ')         
        elif int(svar) != x * y:
            print(f'Du svarade {svar} men rätt svar var {x * y}.')
            svar = input('Vill du spela igen? ')
        elif svar == 'stopp':
            break
    else:
        svar = input('Vill inte längre spela vidare? ')
if rgissningar == 1:
    print(f'Tack för att du spelade, du svarade rätt {rgissningar} gång')
elif rgissningar > 1:
    print(f'Tack för att du spelade, du svarade rätt {rgissningar} gånger')
else:
    print('Antingen försökte du inte spela eller så behöver du träna på din multiplikation')

#uppgift 5a
slut = input('Välj ett väldigt lågt decimaltal: ')
a = 1
n = 0
summa = 0
while a > float(slut):
    summa += a
    n += 1
    a = 1 / (2 ** n)
    print(f'Summan konvergerade till {summa} efter {n} termer')
# uppgift 5b
slut2 = input('Välj ett tal som motsvarar hur många decimaler konvergensen ska vara från 0 innan programmet stannar (förslagsvis max 6 decimaler): ')
a = 1
n = 0
summa = 0
while abs(a) > float(slut2):
    a = ((-1) ** n) / ((2 * n) + 1)
    summa += a
    n += 1
    print(f'Summan konvergerade till {summa} efter {n} termer')