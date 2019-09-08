# Készítsünk programot, amely kiszámolja az első 100 db páratlan szám összegét. (A ciklust vegyük egytől
# százig, majd a ciklusmagban vegyük a ciklusváltozó kétszeresét eggyel csökkentve - így megkapjuk a
# páratlan számokat. Ezeket hasonlóan adjuk össze, mint az első feladatban).

x = 1
for num in range(0,101):
    x += num * 2 - 1

print(x)
