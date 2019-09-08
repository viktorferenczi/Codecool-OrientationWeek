# Készítsünk programot, amely beolvas egy N természetes számot, majd billentyűzetről bekér N db
# természetes számot és a beolvasás után kiírja melyik ezek közül a számok közül a legkisebb. (Ehhez
# vezessünk be egy min nevű változót, melyet mindegyik szám beolvasása után összehasonlítunk a
# számmal, és ha a szám kisebb, akkor megjegyezzük ebben a változóban. A min változót a program
# elején állítsuk be a lehető legnagyobb számra, aminél biztos hogy mindegyik szám kisebb - pl. 32768,
# vagy e helyett a beállítás helyett az első számot olvassuk be (állítsuk be) a min változóba.)



n = int(input("Add meg hány számot szeretnél beírni: "))
min = 99999999

for i in range(n):
    x = int(input("Adj meg egy számot: "))
    if x < min:
        min = x
print(min)




