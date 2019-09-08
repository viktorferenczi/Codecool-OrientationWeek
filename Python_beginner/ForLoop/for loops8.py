# Állítsuk elő és írassuk ki az első N darab Fibonacci-szám összegét: 1 + 1 + 2 + 3 + 5 + 8 + 13 + ...

n = int(input("szám: "))

# változók
number1,number2 = 1,1
my_list = []

#Fibonacci kiírás
for number in range(n-1):
    number1,number2 = number2, number1+number2
    my_list.append(number1)
my_list.insert(0,1)
print(my_list)

#összeg
output = 0
for characters in my_list:
    output += characters
print(output)
