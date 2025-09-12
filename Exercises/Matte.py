import math

b = 3
a = 4
c = 5
d = 7
print('Hypotenusans längd är:', math.sqrt(a**2 + b**2))
print('Kateterns längd är:', math.sqrt(d**2 - c**2))

Gissningar = 365
Rätt = 300
print(f'Modellen har {(Rätt / Gissningar) * 100: .2f}% träffsäkerhet.')

tp = 2
fp = 2
tn = 985
fn = 11
print(f'Modellens träffsäkerhet är {(tp + tn) / (tp + fp + tn + fn) * 100: .2f}%.')


a = (4, 4)
b = (0, 1)
k = (b[1] - a[1]) / (b[0] - a[0])
m = a[1] - k * a[0]
ekvationen = f'y = {k}x + {m}'
print(f'k är {k} och där linjen skär y-axeln är {m}, ekvationen för lutningen av linjen är', ekvationen)

p1 = 3, 5
p2 = -2, 4
dist = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
print(f'Avståndet mellan punkt 1 och punkt 2 är {dist: .2f} längdenheter.')

p1 = 2, 1, 4
p2 = 3, 1, 0
dist = math.sqrt((((p1[0] - p2[0]) ** 2) + (p1[1] - p2[1]) ** 2) + (p1[2] - p2[2]) ** 2)
print(f'Avståndet mellan punkt 1 och punkt 2 är {dist: .2f} längdenheter.')