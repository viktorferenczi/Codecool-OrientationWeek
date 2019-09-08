# A program döntse el, hogy a bekért a , b , c, természetes számok lehetnek-e egy derékszögű
# háromszög oldalhosszúságai. A programot úgy írjuk meg, hogy az a , b , c számok közül bármelyik
# lehet a háromszög átfogója, a maradék kettő pedig a befogók (használjuk Pitagorasz tételét).

num1 = int(input("a: "))
num2 = int(input("b: "))
num3 = int(input("c: "))

if num1 ** 2 + num2 ** 2 == num3 ** 2:
    print("igen")
elif num1 ** 2 + num3 ** 2 == num2 ** 2:
    print("igen")
elif num3 ** 2 + num2 ** 2 == num1 ** 2:
    print("igen")
else:
    print("nem")

