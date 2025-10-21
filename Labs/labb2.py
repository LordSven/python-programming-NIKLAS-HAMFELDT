import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random as rd

datapoints = []
with open('datapoints.txt', 'r') as f:
    next(f)
    for line in f:
        w, h, l = line.strip().split(',')
        datapoints.append((float(w), float(h), int(l)))
width = [w for w, h, l in datapoints]
height = [h for w, h, l in datapoints]
pokemon = [l for w, h, l in datapoints]
pokespec = list(zip(width, height))
pikaw = [25, 24.3, 22]
pikah = [32, 31.5, 34]
pichuw = [20.5]
pichuh = [34]
pikadim = list(zip(pikaw, pikah))
pichudim = list(zip(pichuw, pichuh))
sortpika = []
sortpichu = []
pred = []
def eucdist(td, fd):
    return np.sqrt((td[0] - fd[0])**2 + (td[1] - fd[1])**2)
for ex in pokespec:
    minpika = min(eucdist(ex, ref) for ref in pikadim)
    minpichu = min(eucdist(ex, ref) for ref in pichudim)
    if minpika < minpichu:
        sortpika.append(ex)
        pred.append(1)
    else:
        sortpichu.append(ex)
        pred.append(0)
rättklassad = sum(a == b for a, b in zip(pred, pokemon))
träffsäkerhet = rättklassad / len(pokemon)
plt.scatter(*zip(*pikadim), color='black', marker='P', s=80, label='Pikachu refs')
plt.scatter(*zip(*pichudim), color='black', marker='X', s=75, label='Pichu ref')
plt.scatter(*zip(*sortpika), color='yellow', label='Klassificerad Pikachu')
plt.scatter(*zip(*sortpichu), color='tan', label='Klassificerad Pichu')
plt.xlabel('Width')
plt.ylabel('Height')
plt.legend()
plt.gca().set_aspect('equal')
plt.show()
felklassade = [ex for ex, pred, pok in zip(pokespec, pred, pokemon) if pred != pok]
print(f'Felklassade mot den givna testdatan: {felklassade}.')
print(f'Träffsäkerheten med given testdata är {träffsäkerhet:.2%}')

print('Du har fångat en pokémon men vet inte om det är en pikachu eller en pichu. Följ anvisningarna i din pokédex för att klassificera den.')
while True:
    try:
        bredd = float(input('För in dess bredd i cm: '))
        if not 0 < bredd <= 100:
            raise ValueError('Bredden måste anges i siffror från 1-100.')
        höjd = float(input('För in dess längd i cm: '))
        if not 0 < höjd <= 100:
            raise ValueError('Längden måste anges i siffror från 1-100.')
        break
    except ValueError as err:
        print(err)
pokedex = (bredd, höjd)
def kNP(point, pokespec, pokemon, k=10):
    dists = [(eucdist(point, other), other, klass) for other, klass in zip(pokespec, pokemon)]
    dists.sort(key=lambda x: x[0])
    nearest = [(other, klass) for _, other, klass in dists[:k]]
    predklass = Counter([klass for _, klass in nearest]).most_common(1)[0][0]
    return nearest, predklass
kNPpred = [kNP(ex, pokespec, pokemon, k=10)[1] for ex in pokespec]
rättklassade_kNP = sum(a == b for a, b in zip(kNPpred, pokemon))
träffsäkerhet_kNP = rättklassade_kNP / len(pokemon)
felklassade_kNP = [ex for ex, pred, pok in zip(pokespec, kNPpred, pokemon) if pred != pok]
print(f'Felklassade efter kNP (k=10): {felklassade_kNP}.')
print(f'Träffsäkerheten med kNP (k=10) är {träffsäkerhet_kNP:.2%}.')
neighbors, kNPpred = kNP(pokedex, pokespec, pokemon, k=10)
x_pika = [x for (x, y), klass in zip(pokespec, pokemon) if klass == 1]
y_pika = [y for (x, y), klass in zip(pokespec, pokemon) if klass == 1]
x_pichu = [x for (x, y), klass in zip(pokespec, pokemon) if klass == 0]
y_pichu = [y for (x, y), klass in zip(pokespec, pokemon) if klass == 0]
plt.scatter(x_pika, y_pika, color='yellow', label='Pikachu')
plt.scatter(x_pichu, y_pichu, color='tan', label='Pichu')
plt.scatter(*pokedex, color='red', marker='*', s=80, label='Det var en Pikachu' if kNPpred == 1 else 'Det var en Pichu')
for (pt, lab) in neighbors:
    plt.scatter(*pt, edgecolors='black', facecolors='none', s=300, linewidths=2, label='Nearest pokémon' if neighbors.index((pt, lab)) == 0 else '')
plt.legend()
plt.gca().set_aspect('equal')
plt.show()

accuracy = []
def slumpad_klassificering():
    pikachu = [(w, h) for w, h, l in datapoints if l == 1]                                        # delar upp testdatan utifrån klasserna
    pichu  = [(w, h) for w, h, l in datapoints if l == 0]                                         # delar upp testdatan utifrån klasserna
    train_pikachu = rd.sample(pikachu, 50)                                                      # slumpar fram 50 pikachu-punkter för träningsdata
    train_pichu  = rd.sample(pichu, 50)                                                         # slumpar fram 50 pichu-punkter för träningsdata
    test_pikachu = [p for p in pikachu if p not in train_pikachu]                               # tilldelar resterande 25 pikachu-punkter till testdata
    test_pichu  = [p for p in pichu if p not in train_pichu]                                    # tilldelar resterande 25 pichu-punkter till testdata
    train_data = [(x, y, 1) for x, y in train_pikachu] + [(x, y, 0) for x, y in train_pichu]    # slår ihop träningspikachu och träningspichu till en lista
    test_data = [(x, y, 1) for x, y in test_pikachu]  + [(x, y, 0) for x, y in test_pichu]      # slår ihop testpikachu och testpichu till en lista
    train_dim_0 = [(x, y) for (x, y, label) in train_data if label == 0]                        # separerar dimensioner från label för att kunna jämföra euklidisk distans
    train_dim_1 = [(x, y) for (x, y, label) in train_data if label == 1]                        # separerar dimensioner från label för att kunna jämföra euklidisk distans
    pred = []
    for (x, y, label) in test_data:
        minpika = min(eucdist((x, y), ref) for ref in train_dim_1)                              # räknar ut euklidisk distans
        minpichu = min(eucdist((x, y), ref) for ref in train_dim_0)                             # räknar ut euklidisk distans
        if minpika < minpichu:                                                                  # utför jämförelsen
            pred.append(1)                                                                      # sparar om pikachu förutspås
        else:
            pred.append(0)                                                                      # sparar om pichu förutspås
    rättklassad = [label for (_, _, label) in test_data]                                        # jämför sedan förutspådda klasser mot faktiska från den slumpade testdatan
    accuracy.append(sum(p == t for p, t in zip(pred, rättklassad)) / len(rättklassad))          # räknar ut träffsäkerhet av förutspåelserna
for i in range(10):                                                                             # utför 10 iterationer av nya slumpningar
    slumpad_klassificering()
medelträffsäkerhet = sum(accuracy) / len(accuracy)
print(f'Medelträffsäkerhet med slumpmässigt utvalda träningspunkter och testpunkter: {medelträffsäkerhet:.2%}')
plt.plot(range(1, 11), accuracy, '-o')
plt.axhline(y=medelträffsäkerhet, color='orange', label=f'Medelträffsäkerhet = {medelträffsäkerhet:.2%}')
plt.xlabel('Iteration')
plt.ylabel('Träffsäkerhet')
plt.legend()
plt.show()