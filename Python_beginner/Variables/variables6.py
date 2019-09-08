import math, sys

# A program kérjen be egy pénzösszeget, majd határozza meg, és írja ki, hogy hogyan fizethetjük ki a
# lehető legkevesebb 10, 5, 2 és 1 koronás érmével (használjuk a maradékos osztás % és egész osztás
# // műveleteket)!

amount = int(input("Ird be az értéket: "))

coin = [10, 5, 2, 1]

print("A lehető legkevesebb érme ebben az esetben:")
for i in range(len(coin)):
    while amount >= coin[i]:
        amount = amount - coin[i]
        print(coin[i])







