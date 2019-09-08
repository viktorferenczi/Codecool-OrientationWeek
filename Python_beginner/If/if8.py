# Egészítsük ki az előző programunkat úgy, hogy a beolvasás után a számok közül ne csak a legkisebbet,
# de a legnagyobbat is írja ki. (Ehhez vezessünk be egy max nevű változót, melyet mindegyik szám
# beolvasása után összehasonlítunk a számmal, és ha a szám nagyobb, akkor megjegyezzük ebben a
# változóban. A max változót a program elején állítsuk be a lehető legkisebb számra, aminél biztos hogy
# mindegyik szám nagyobb - pl. –32767, vagy ez helyett a beállítás helyett az első számot olvassuk be
# (állítsuk be) a max változóba.)

n = int(input("Add meg hány számot szeretnél beírni: "))
min = 99999999
max = -99999999

for i in range(n):
    x = int(input("Adj meg egy számot: "))
    if x < min:
        min = x
    if x > max:
        max = x

print(min)
print(max)