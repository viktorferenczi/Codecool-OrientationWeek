# Kérjünk be N darab természetes számot (először N -t kérjük be). Az adatok beírása után a program
# írja ki a páros és páratlan számok darabszámát, és a páratlan számok összegét!


#input bekérés

try:
    my_list = []
    paros_szam = []
    paratlan_szam = []
    while True:
        my_list.append(int(input("Give me a list of numbers, press " "Enter" " after the number, "
                                "type ""Stop" " to finish it:  ")))
except:
   pass


#páros vagy páratlan

for char in my_list:
    if char % 2 == 0:
        paros_szam.append(char)
    else:
        paratlan_szam.append(char)

x = len(paros_szam)
y = len(paratlan_szam)


print(x)
print(y)

#páratlan számok összeadása

z = 0
for char in paratlan_szam:
    z += char
print(z)





