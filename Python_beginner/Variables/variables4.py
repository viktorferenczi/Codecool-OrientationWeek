# A program kérjen be egy számot, majd írja ki a kis szorzótáblát erre a számra (1-től 5-ig). A program a
# beolvasás után hagyjon ki egy üres sort.

x = input("Please give me a number: ")
print('')

result = print(x + "*0=", int(x) * 0,
               x + "*1=", int(x) * 1,
              x + "*2=", int(x) * 2,
              x + "*3=", int(x) * 3,
              x + "*4=", int(x) * 4,
              x + "*5=", int(x) * 5,)