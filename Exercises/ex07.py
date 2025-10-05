# uppgift 1
#
#impor numpy as np              fel:"impor" istället för import
#
#def distance(x,y)              fel: saknar ":"
#    reurn np.sqrt(x+y)         fel: "reurn" istället för return samt att x och y behöver vara upphöjda med 2
#
#print(distance([0.5, 0.5]))    fel: koordinaterna inuti en lista, antingen tar man bort [] eller så gör man listan utanför print/funktionen och sedan *listan i print/funktionen
#
# korrekt version
import numpy as np
def distance(x, y):
    return np.sqrt(x**2 + y**2)
print(distance(0.5, 0.5))

# uppgift 2
#
#def is_fourdigit(number):
#    if number//1000 < 10       fel: alla negativa tal ger True och att använda // leder till fel om man använder abs() som lösning, därav vanlig division i min lösning
#        return true            fel: behöver vara stort T i True
#    else 
#        return false           fel: behöver vara stort F i False
#
# korrekt version
def is_fourdigit(number):
    if abs(number / 1000) < 10 and abs(number / 1000) >= 1:
        return True
    else:
        return False
test_numbers = [231, 3124, -4124, -1000,-999, 1001, 10000, -10000, 999]
for number in test_numbers:
    if is_fourdigit(number):
        print(f"{number} is four-digit")
    else:
        print(f"{number} is not four-digit")

# uppgift 3
while True:
    try:
        åk = input('Hur ofta reser du med spårvagnen per månad? ')
        åk = int(åk)
        try:
            if åk < 0 or åk > 200:
                raise ValueError
            else:
                break
        except ValueError:
            print('Rimligtvis bör du ta vagnen mellan 0-200 gånger per månad, svara någonstans inom det spannet.')                  
    except ValueError:
        print('Antalet resor måste anges i heltal med siffror.')
while True:
    try:
        biljett = input('Vad kostar biljetten vid varje resa? ')
        biljett = float(biljett)
        try:
            if biljett < 0 or biljett > 100:
                raise ValueError
            else:
                break
        except ValueError:
            print('Rimligtvis bör en korttidsbiljett kosta mellan 0-100kr, svara någonstans inom det spannet.')
    except ValueError:
        print('Biljettpris måste anges med siffror.')
while True:
    try:
        månadskort = input('Vad kostar ett månadskort? ')
        månadskort = float(månadskort)
        try:
            if månadskort < 500 or månadskort > 1500:
                raise ValueError
            else:
                break
        except ValueError:
            print('Rimligtvis bör månadskortet kosta mellan 500-1500kr, svara någonstans inom det spannet.')
    except ValueError:
        print('Månadskortets kostnad måste anges med siffror.')
biljettkostnad = åk * biljett
if biljettkostnad > månadskort:
    print(f'Om du skulle betala för biljett {åk} gånger så vore det mer värt att köpa månadskort för {månadskort}kr då biljetterna skulle kostat {biljettkostnad}kr så du sparar då {biljettkostnad - månadskort}kr.')
elif biljettkostnad < månadskort:
    print(f'Om du bara kommer att betala för biljett {åk} gånger så är det mer värt att köpa biljett vid varje åk, du sparar då {månadskort - biljettkostnad}kr gentemot att betala {månadskort}kr för ett månadskort.')
else:
    print(f'Om du skulle köpa biljett {åk} gånger så blir kostnaden för det lika stor som för ett månadskort så personligen hade jag valt det senare.')