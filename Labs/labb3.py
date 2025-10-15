import matplotlib.pyplot as plt
import numpy as np
import random as rd
import csv

coords = []
x, y = zip(*coords)
xmean = (sum(x) / len(x))
ymean = (sum(y) / len(y))
k = ymean / (xmean * -1)
m = ymean - k * xmean
xlinje = [min(x), max(x)]
ylinje = [k*xval + m for xval in xlinje]
sort1 = []
sort0 = []
def above_or_below(x, y, k, m):
    if y > k * x + m:
        sort1.append((x, y))
    else:
        sort0.append((x, y))
for ex in coords:
    punktA = above_or_below(ex[0], ex[1], k, m)
x1, y1 = zip(*sort1)
x0, y0 = zip(*sort0)
def plotta():
    plt.plot(xlinje, ylinje, color='red', label='Divider')
    plt.scatter(x1, y1, color='blue', s=20, label='Kluster 1')
    plt.scatter(x0, y0, color='purple', s=20, label='Kluster 0')
    plt.title('Linjär klassificering')
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.show()
plotta()
klassificerade = []
with open('unlabelled_data.csv', 'r') as unlabelled_data:
    for line in unlabelled_data:
        x, y = line.strip().split(',')
        coords.append((float(x), float(y)))


for ex in sort1:
    klassificerade.append((ex[0], ex[1], 1))
for ex in sort0:
    klassificerade.append((ex[0], ex[1], 0))
with open('labelled_data.csv', 'w', newline='', encoding='utf-8') as labelled_data:
    writer = csv.writer(labelled_data)
    writer.writerow(['x-koordinat', 'y-koordinat', 'klass (1 = över, 0 = under)'])
    for x, y, klass in klassificerade:
        writer.writerow([x, y, klass])