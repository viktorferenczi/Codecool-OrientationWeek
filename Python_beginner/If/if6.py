# Olvassunk be egy szöveget, majd írassuk ki a képernyőre a beolvasott szövegből az összes < és >
# jelek közé írt részeket, mindegyiket új sorba.

statement = input("Adj meg egy mondatot: ")
new_statement = ""


write = False

for letter in statement:
    if letter == "<":
        write = True
    if letter == ">":
        write = False
    if write == True:
        new_statement += letter

for letter in new_statement:
    if letter == "<":
        new_statement = new_statement.replace("<", "\n")

print(new_statement)



