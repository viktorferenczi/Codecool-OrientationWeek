# Határozzuk meg és írassuk ki az összes hárommal és öttel egyaránt osztható, 1000-nél kisebb
# természetes számot.

def five_three_divided():
    x = ""
    for num in range(1,1000):
        if num % 3 == 0 and num % 5 == 0:
            print(num)

five_three_divided()
