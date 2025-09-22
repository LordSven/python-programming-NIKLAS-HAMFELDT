# uppgift 1a
import random as rd
list = []
for a in range(10):
    dr = rd.randint(1, 6)
    list.append(dr)
list.sort()
print(list)
# uppgift 1b
list = []
for a in range(10):
    dr = rd.randint(1, 6)
    list.append(dr)
list.sort(reverse=True)
print(list)
# uppgift 1c
list = []
for a in range(10):
    dr = rd.randint(1, 6)
    list.append(dr)
h = max(list)
l = min(list)
print(list)
print(f'Det högsta slaget var {h}\nDet lägsta slaget var {l}')

# uppgift 2a
middagsval = ['Vegetarisk lasagne', 'Spaghetti', 'Fisk', 'Grönsakssoppa', 'Pannkakor']
# uppgift 2b
veckodagar = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag']
# uppgift 2c
print(f'{veckodagar[0]}: {middagsval[0]}'
      f'\n{veckodagar[1]}: {middagsval[1]}'
      f'\n{veckodagar[2]}: {middagsval[2]}'
      f'\n{veckodagar[3]}: {middagsval[3]}'
      f'\n{veckodagar[4]}: {middagsval[4]}'
      )

# uppgift 3a
import matplotlib.pyplot as plt
kvadrater = [x**2 for x in (range(-10, 11))]
# uppgift 3b
x = [x**2 for x in (range(-10, 11))]
y = [y + 1 for y in (range(-10, 11))]
plt.plot(y, x)
plt.title('Plot list comprehension')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# uppgift 4a
filer = 'ABCDEFGH'
ranker = '12345678'
print(f'{filer[0]}{ranker[0]} {filer[1]}{ranker[0]} {filer[2]}{ranker[0]} {filer[3]}{ranker[0]} {filer[4]}{ranker[0]} {filer[5]}{ranker[0]} {filer[6]}{ranker[0]} {filer[7]}{ranker[0]}')
# uppgift 4b
for r in ranker[::-1]:
    rad = [f + r for f in filer]
    print(' '.join(rad))

# uppgift 5a
diro = 0
nr6 = 0
for x in range(100):
    roll = rd.randint(1, 6)
    diro += 1
    if roll == 6:
        nr6 += 1
print(f'Nummer 6 blev slaget {nr6} gånger av {diro} tärningsslag.')
# uppgift 5b
results = []
diro = 0
nr6 = 0
for x in range(10):
    roll = rd.randint(1, 6)
    diro += 1
    if roll == 6:
        nr6 += 1
print(f'På 10 slag var det {(nr6 / 10) * 100: .2f}% chans att få en sexa.')
results.append(nr6 * 10)
nr6 = 0
diro = 0
for x in range(100):
    roll = rd.randint(1, 6)
    diro += 1
    if roll == 6:
        nr6 += 1
print(f'På 100 slag var det {(nr6 / 100) * 100: .2f}% chans att få en sexa.')
results.append(nr6)
nr6 = 0
diro = 0
for x in range(1000):
    roll = rd.randint(1, 6)
    diro += 1
    if roll == 6:
        nr6 += 1
print(f'På 1000 slag var det {(nr6 / 1000) * 100: .2f}% chans att få en sexa.')
results.append(nr6 / 10)
nr6 = 0
diro = 0
for x in range(10000):
    roll = rd.randint(1, 6)
    diro += 1
    if roll == 6:
        nr6 += 1
print(f'På 10000 slag var det {(nr6 / 10000) * 100: .2f}% chans att få en sexa.')
results.append(nr6 / 100)
nr6 = 0
diro = 0
for x in range(100000):
    roll = rd.randint(1, 6)
    diro += 1
    if roll == 6:
        nr6 += 1
print(f'På 100000 slag var det {(nr6 / 100000) * 100: .2f}% chans att få en sexa.')
results.append(nr6 / 1000)
nr6 = 0
diro = 0
for x in range(1000000):
    roll = rd.randint(1, 6)
    diro += 1
    if roll == 6:
        nr6 += 1
print(f'På 1000000 slag var det {(nr6 / 1000000) * 100: .2f}% chans att få en sexa.')
results.append(nr6 / 10000)
print(results)
x_indices = range(len(results))
xlabels = [10, 100, 1000, 10000, 100000, 1000000]
ylabels = [0, 10, 20, 30, 40, 50]
plt.plot(x_indices, results, '-*')
plt.title('Trolighet för att slå en sexa på x antal slag')
plt.xticks(x_indices, xlabels)
plt.yticks(ylabels)
plt.xlabel('Antal tärningsslag')
plt.ylabel('Trolighet')
plt.show()

# uppgift 6a
import numpy as np
coord = []
eucdist = []
träff = []
miss = []
träffar = 0
for i in range(5000):
    x = rd.uniform(-1, 1)
    y = rd.uniform(-1, 1)
    addcoord = (x, y)
    coord.append(addcoord)
for (x, y) in coord:
    dist = np.sqrt(x**2 + y**2)
    eucdist.append(dist)
    if dist < 1:
        träff.append((x, y))
        träffar += 1
    else:
        miss.append((x, y))
xt, yt = zip(*träff)
xm, ym = zip(*miss)
plt.scatter(xt, yt, color='blue', s=5)
plt.scatter(xm, ym, color='red', s=5)
plt.gca().set_aspect('equal')
plt.show()
# uppgift 6b
print(f'Chans för träff är {träffar / 5000: .4f}') # vilket bör konvergera till pi/4

# uppgift 7a
print(f'Jag byter dörr för när jag först valde så hade jag 33% chans att välja rätt men när jag nu väljer så har jag')
# uppgift 7b
