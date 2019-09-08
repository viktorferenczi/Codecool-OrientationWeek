# A program döntse el, hogy a bekért a , b , c természetes számok lehetnek-e egy derékszögű
# háromszög oldalhosszúságai. Az a és b legyen a két befogó (használjuk Pitagorasz tételét).
# (c az átfogó):  a^2+b^2=c^2


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a ** 2 + b ** 2 == c ** 2:
    print("lehet")
else:
    print("nem")




