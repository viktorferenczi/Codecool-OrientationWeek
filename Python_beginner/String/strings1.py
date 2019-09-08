# Készítsünk programot, amely bekér egy mondatot, majd kiírja ugyanezt a mondatot úgy, hogy mindegyik
# betű (karakter) után kirak egy szóközt.

prompt = input("Give me a sentence: ")

s = " "
new_result = " "

for letter in prompt:
    new_result = new_result + letter + s
print(new_result)
