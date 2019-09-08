# Kérjünk be egy mondatot. Számoljuk meg és írassuk ki, hogy hány szóköz van benne.

prompt = input("Give me a sentence: ")

if " " in prompt:
    x = prompt.count(" ")
print(x)