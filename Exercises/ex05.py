import matplotlib.pyplot as plt
import random as rd
import numpy as np
dörr = [1, 2, 3]
for i in range(1000):
    kanin = rd.randint(1, 3)
    val = rd.randint(1, 3)
    while val == kanin:
        val = rd.randint(1, 3)
    if kanin == 1 and val == 2:
        dörr.remove(3)
    elif kanin == 1 and val == 3:
        dörr.remove(2)
    elif kanin == 2 and val == 1:
        dörr.remove(3)
    elif kanin == 2 and val == 3:
        dörr.remove(1)
    elif kanin == 3 and val == 1:
        dörr.remove(2)
    else:
        dörr.remove(1)
    print('k', kanin)
    print('v', val)
    print('d', dörr)
    
    dörr = [1, 2, 3]