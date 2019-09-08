# Készítsen programot faktoriális számolásra.
from math import factorial

prompt = input("Adj meg egy számot: ")
x = int(prompt)

print(factorial(x))

n2 = int(input("Adj meg egy számot: "))
y = 1
for number in range(1,n2+1):
    y = y * number

print(y)