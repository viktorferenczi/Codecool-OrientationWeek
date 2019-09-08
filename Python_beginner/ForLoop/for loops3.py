# Készítsünk programot, amely kiszámolja az első 100 db páros szám összegét. (A ciklust vegyük egytől
# százig, majd a ciklusmagban vegyük a ciklusváltozó kétszeresét - így megkapjuk a páros számokat.
# Ezeket hasonlóan adjuk össze, mint az első feladatban.)

x = 1
for num in range(1,101):
    x += num * 2

print(x)