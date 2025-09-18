# uppgift 1a
for i in range(-10, 11):
    print(i, end=' ')
print()
# uppgift 1b
for i in range(-10, 11, 2):
    print(i, end=' ')
print()

# uppgift 2a
n = 0
a = 0
for n in range(99):
    n += 1
    a += n
    print(f'{n} +', end=' ')
print(f'100 = {a + 100}')
# uppgift 2b
n = 1
a = 0
for n in range(0, 97, 2):
    n += 1
    a += n
    print(f'{n} +', end=' ')
print(f'99 = {a + 99}')

# uppgift 3a
a = 0
b = 6
for a in range(10):
    a += 1
    b = 6 * a
    print(f'{a} * 6 = {b}')
# uppgift 3b
x = int(input('Vilket tal vill du ha multiplikationstabellen för? '))
a = int(input('Hur många exempel ska ingå i tabellen? '))
b = int(input('Hur lågt ska tabellen börja? '))
for a in range(a):
    b += 1
    a = x * (b - 1)
    print(f'{b - 1} * {x} = {a}')
# uppgift 3c
for x in range(11):
    for y in range(11):
        print(f'|{x * y: 4}', end=' ')
    print('|')

# uppgift 4
n = int(input('Skriv ett tal: '))
summa = 1
for a in range(1, n + 1):
    summa *= a
print(summa)

# uppgift 5
import random
tal = random.randint(1000, 9999)
for a in range(10000):
    if a == tal:
        print(f'Datorn gissar på {a}')
print(f'Rätt svar var {tal}')

# uppgift 6
ris = 1
for x in range(8):
    for y in range(8):
        ris *= 2
print(f'När schackbrädets sista ruta fyllts skulle det ha {ris - 1} riskorn på.')