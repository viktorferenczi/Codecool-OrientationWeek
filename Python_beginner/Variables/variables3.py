# Írjunk programot, amely beolvas két természetes számot, majd kiírja a két szám hányadosát és
# maradékát az alábbi formában. A program az adatok beolvasása után hagyjon ki egy üres sort.

x = float(input("Első szám: "))
y = float(input("Második szám: "))

print("")
eredmeny = print("hányados: ",int(x / y), "maradék: ", x % y)