# uppgift 1a
import random as rd
with open('dice_rolls.txt', 'a') as dice_rolls:
    rolls = []
    fyror = 0
    for a in range(20):
        roll = rd.randint(1, 6)
        rolls.append(roll)
        if roll == 4:
            fyror += 1
    dice_rolls.write(f'Uppgift 1a)\n20 simulerade tärningsslag gav detta resultat: {' '.join(str(roll) for roll in rolls)}\n')
# uppgift 1b
    rolls.sort()
# uppgift 1c
    dice_rolls.write(f'\nUppgift 1b)\nSorterat i storleksordning är det: {' '.join(str(roll) for roll in rolls)}\n\nUppgift 1c)\nAntal fyror slagna: {fyror}')

# uppgift 2a
with open('test_result.txt', 'r', encoding='utf-8') as test_result:
    print(test_result.read())
# uppgift 2b
with open('test_result.txt', 'a+', encoding='utf-8') as test_result:
    test_result.seek(0)
    lista = test_result.readlines()
    uppradat = [line.strip() for line in lista]
    uppradat.sort()
    nylista = '\n'.join(uppradat)
    test_result.write(f'\n\nSorterat\n{nylista}')
# uppgift 2c
    uppradat = [line.strip() for line in lista]
    kolumner = [kolumn.split() for kolumn in uppradat if not kolumn.startswith('Sorterat')]
    for betyg in kolumner:
        if int(betyg[-1]) < 20:
            betyg.append('F')
        elif int(betyg[-1]) >= 20 and int(betyg[-1]) <= 29:
            betyg.append('E')
        elif int(betyg[-1]) >= 30 and int(betyg[-1]) <= 39:
            betyg.append('D')
        elif int(betyg[-1]) >= 40 and int(betyg[-1]) <= 49:
            betyg.append('C')
        elif int(betyg[-1]) >= 50 and int(betyg[-1]) <= 59:
            betyg.append('B')
        elif int(betyg[-1]) >= 60 and int(betyg[-1]) <= 70:
            betyg.append('A')
    kolumner.sort(key=lambda x: x[-1])
    betygsatt = '\n'.join([' '.join(betyg) for betyg in kolumner])
    test_result.write(f'\n\nBetygsatt\n{betygsatt}')

# uppgift 3
import matplotlib.pyplot as plt
with open('NPvt19Ma2A.txt', 'r') as fil1, open('NPvt19Ma2C.txt', 'r') as fil2:
    paj1 = [line.strip(' \n%') for line in fil1]
    paj2 = [line.strip(' \n%') for line in fil2]
    betyg1 = [x.split()[0] for x in paj1]
    andel1 = [float(y.split()[1]) for y in paj1]
    betyg2 = [x.split()[0] for x in paj2]
    andel2 = [float(y.split()[1]) for y in paj2]
    renbetyg1 = [b for b, a in zip(betyg1, andel1) if a > 0]
    renandel1 = [a for a in andel1 if a > 0]
    etiketter1 = [f"{b} ({a:.1f}%)" for b, a in zip(renbetyg1, renandel1)]
    etiketter2 = [f"{b} ({a:.1f}%)" for b, a in zip(betyg2, andel2)]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    ax1.pie(renandel1, labels=renbetyg1, autopct='%1.1f%%', startangle=90, radius=0.6)
    ax1.set_title('Betygsfördelning Ma2A')
    ax1.legend(etiketter1, title='Betygsfördelning Ma2A', loc='upper left', bbox_to_anchor=(0, 1))
    ax2.pie(andel2, labels=betyg2, autopct='%1.1f%%', startangle=90, radius=0.6)
    ax2.set_title('Betygsfördelning Ma2C')
    ax2.legend(etiketter2, title='Betygsfördelning Ma2C', loc='upper left', bbox_to_anchor=(0, 1))
    plt.show()

# uppgift 4
import random as rd
from collections import Counter
with open('simulation.txt', 'a') as simulation:
    def slå_tärning(slag):
        diro = []
        dirocount = []
        for x in range(slag):
            diro.append(rd.randint(1, 6))
        counts = Counter(diro)
        for x in range(1, 7):
            dirocount.append(f'Antal {x}or: {counts[x]}, chans: {counts[x] / slag * 100: .2f}%')
        return '\n'.join(dirocount)   
    simulation.write(f'10 slag:\n{slå_tärning(10)}\n\n')
    simulation.write(f'100 slag:\n{slå_tärning(100)}\n\n')
    simulation.write(f'1000 slag:\n{slå_tärning(1000)}\n\n')
    simulation.write(f'10000 slag:\n{slå_tärning(10000)}\n\n')
    simulation.write(f'100000 slag:\n{slå_tärning(100000)}\n\n')