import numpy as np
import matplotlib.pyplot as plt
import random as rd

datapoints = []
with open('datapoints.txt', 'r') as f:
    next(f)
    for line in f:
        w, h, l = line.strip().split(',')
        datapoints.append((float(w), float(h), int(l)))
accuracy = []
def eucdist(td, fd):
    return np.sqrt((td[0] - fd[0])**2 + (td[1] - fd[1])**2)
def slumpad_klassificering():
    pikachu = [(w, h) for w, h, l in datapoints if l == 1]                                      # delar upp testdatan utifrån klasserna
    pichu  = [(w, h) for w, h, l in datapoints if l == 0]                                       # delar upp testdatan utifrån klasserna
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
plt.plot(range(1, 11), accuracy, '-o')
plt.axhline(y=medelträffsäkerhet, color='orange', label=f'Medelträffsäkerhet = {medelträffsäkerhet:.2%}')
plt.xlabel('Iteration')
plt.ylabel('Träffsäkerhet')
plt.legend()
plt.show()