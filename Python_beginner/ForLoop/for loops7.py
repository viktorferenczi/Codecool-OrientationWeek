# Állítsuk elő és írassuk ki az első N darab Fibonacci-számot. Ennek a sorozatnak az a jellemzője, hogy
# bármelyik eleme egyenlő az előző kettő összegével. A sorozat néhány eleme: 1, 1, 2, 3, 5, 8, 13, ...

n = int(input("szám: "))
number1,number2 = 1,1

print(number1) # 1 kezdődik

for letter in range(n-1):
    number1,number2 = number2, number1+number2
    print(number1)