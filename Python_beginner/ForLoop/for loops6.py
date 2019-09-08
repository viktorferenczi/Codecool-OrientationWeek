# Kérjünk be két természetes számot ( M , N ), majd rajzoljunk ki a képernyőre egy M x N méretű
# téglalapot csillag ( * ) jelekből úgy, hogy a téglalap belseje üres legyen. (Aka.: disznó ól csillagból
# feladat.)


width = int(input("Width: "))
length = int(input("Length: ")) -2
wid = ""
leng = ""
star = "*"
space =" "

for number in range(width):
    wid = wid + star

print(wid)
width2 = width -2

for number in range(length):
    leng = print(star + (space * width2) + star)
print(wid)



