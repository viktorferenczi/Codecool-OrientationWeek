# Almát szeretnénk vásárolni. Írjunk egy programot, amely billentyűzetről kérje be először azt, hogy
# mennyibe kerül egy kilogramm alma, majd azt hogy hány kilogramm almát szeretnénk venni. A program
# számolja ki, hogy ennyi almáért hány koronát fogunk fizetni.

while True:
    try:
        how_much = int(input("How much 1kg apple worth? "))
        how_many = int(input("How many apples would like to buy? "))
        break
    except ValueError:
        print("Please use numbers.")
price = int(how_much) * int(how_many)
print("You have to pay " + str(price) + " korona")





