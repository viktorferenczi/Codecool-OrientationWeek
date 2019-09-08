# Olvassunk be egy a természetes számot és egy ch karaktert. Rajzoljunk ki a beolvasott karakterből
# egy a oldalú négyzetet a képernyőre (minden sorban a db karakter legyen és összesen a db
# sorunk legyen) egymásba ágyazott cilusok segítségével.

prompt = input("give me a char: ")
prompt2 = int(input("give me a number: "))

while True:
    for number in range(prompt2):
        result = (prompt * prompt2)
        print(result)
        if result == prompt2:
            break
    break




