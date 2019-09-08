# Készítsünk programot, amely kiszámolja az első 7 db természetes szám szorzatát egy ciklus segítségével.
# (A szorzat kiszámolásához vezessünk be egy változót, amelyet a program elején beállítunk 1-re, a
# ciklusmagban pedig mindig hozzászorozzuk a ciklusváltozó értékét, tehát sorban az 1, 2, 3, ..., 7
# számokat.)

x = 1

for num in range(1, 8):
    x = x * num

print(x)