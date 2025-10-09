import matplotlib.pyplot as plt
import numpy as np
import random as rd
import csv

with open('unlabelled_data.csv', 'r') as rådata:
    lines = rådata.readlines()
    coords = [line.strip() for line in lines]
    floatcoords = [tuple(map(float, coord.split(','))) for coord in coords]
    x, y = zip(*floatcoords)
    center1 = (2.44, 2.22)
    center0 = (-2.44, -2.22)
    sort1 = []
    sort0 = []
    xmean, ymean = (center1[0] + center0[0]) / 2, (center1[1] + center0[1]) / 2
    k = (center0[1] - center1[1]) / (center0[0] - center1[0])
    m = center1[1] - k * center1[0]
    k2 = -1 / k
    m2 = ymean - k2 * xmean
    xlinje = [min(x), max(x)]
    ylinje = [k2*xval + m2 for xval in xlinje]
    def eucdist(td, fd):                                                                # taget från labb2
        return np.sqrt((td[0] - fd[0])**2 + (td[1] - fd[1])**2)
    for ex in floatcoords:
        punktA = eucdist(ex, center1)
        punktB = eucdist(ex, center0)
        if punktA < punktB:
            sort1.append(ex)
        else:
            sort0.append(ex)
    x1, y1 = zip(*sort1)
    x0, y0 = zip(*sort0)
    true_x1, true_y1 = sum(x1) / len(x1), sum(y1) / len(y1)
    true_x0, true_y0 = sum(x0) / len(x0), sum(y0) / len(y0)
    true_center1 = (true_x1, true_y1)
    true_center0 = (true_x0, true_y0)
    true_xmean, true_ymean = (true_center1[0] + true_center0[0]) / 2, (true_center1[1] + true_center0[1]) / 2
    k3 = -1 / ((true_center0[1] - true_center1[1]) / (true_center0[0] - true_center1[0]))
    m3 = true_ymean - k3 * true_xmean                                                     
    true_xlinje = [min(x), max(x)]
    true_ylinje = [k3*xval + m3 for xval in true_xlinje]
    def plotta(test=None):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        ax1.plot(xlinje, ylinje, color='red', label='Estimated divider')
        ax1.scatter(x1, y1, color='blue', label='Cluster 1')
        ax1.scatter(x0, y0, color='purple', label='Cluster 0')
        if test is not None:
            ax1.scatter(test[0], test[1], color='black', s=100, marker='X', label='Input coordinate')
        ax1.set_aspect('equal')
        ax1.set_title('Uppskattad divider')
        ax1.legend()
        ax2.plot(true_xlinje, true_ylinje, color='green', label='True divider')
        ax2.scatter(x1, y1, color='blue', label='Cluster 1')
        ax2.scatter(x0, y0, color='purple', label='Cluster 0')
        if test is not None:
            ax2.scatter(test[0], test[1], color='black', s=100, marker='X', label='Input coordinate')
        ax2.set_aspect('equal')
        ax2.set_title('Träffsäker divider')
        ax2.legend()
        plt.tight_layout()
        plt.show()
    def above_or_below(xpunkt, ypunkt, k, m):
        if ypunkt > k3 * xpunkt + m3:
            print('Punkten var ovanför linjen.')
        else:
            print('Punkten var under linjen.')
        plotta((xpunkt, ypunkt))
    while True:
        test = input('Ange en koordinat att testa eller ange "Random" för att testa en slumpmässig punkt ur listan: ')
        if test.lower() == 'random':
            test = rd.choice(floatcoords)
            print(test)
            above_or_below(test[0], test[1], k3, m3)
            break
        elif ',' in test:
            try:
                test = tuple(map(float, test.split(',')))
                above_or_below(test[0], test[1], k3, m3)
                break
            except ValueError:
                print('Svaret måste anges som antingen "Random" eller i koordinatform x, y.')
        else:
            print('Svaret måste anges som antingen "Random" eller i koordinatform x, y.')
    klassificerade = []
    for ex in sort1:
        klassificerade.append((ex[0], ex[1], 1))
    for ex in sort0:
        klassificerade.append((ex[0], ex[1], 0))
    with open('labelled_data.csv', 'w', newline='') as labelled_data:
        writer = csv.writer(labelled_data)
        writer.writerow(['x-koordinat', 'y-koordinat', 'klass'])
        for x, y, klass in klassificerade:
            writer.writerow([x, y, klass])