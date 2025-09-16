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
print('3a) ',end=' ')
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