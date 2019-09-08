import math, sys

# Kérjünk be két, egy napon belüli, időpontot (először az órát, aztán a percet, végül a másodpercet).
# Számítsuk ki a két időpont közti különbséget másodpercekben és írassuk ki!

x = int(input("Please give me an hour:"))
y = int(input("please give a minute:"))
z = int(input("please give me a sec"))
x2 = int(input("Please give me an hour:"))
y2 = int(input("please give a minute:"))
z2 = int(input("please give me a sec"))

time1 = (x * 3600 + y * 60 + z)
time2 = (x2 * 3600 + y2 * 60 + z2)

if time1 > time2:
    print(time1 - time2)
else:
    print(time2 - time1)



