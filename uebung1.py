zahl1 = input("Zahl 1: ")
zahl2 = input("Zahl 2: ")
zahl3 = input("Zahl 3: ")


if(zahl1 < zahl2 < zahl3):
    print(zahl1)
    if(zahl2 < zahl3):
        print(zahl2)
    if(zahl3 < zahl2):
        print (zahl3)
    if(zahl3 > zahl2):
        print(zahl3)
    if(zahl2 > zahl3):
        print(zahl2)

if(zahl2 < zahl1 < zahl3):
    print(zahl2)
    if(zahl1 < zahl3):
        print(zahl1)
    if(zahl3 < zahl1):
        print (zahl3)
    if(zahl3 > zahl1):
        print(zahl3)
    if(zahl1 > zahl3):
        print(zahl1)

if(zahl3 < zahl2 < zahl1):
    print(zahl3)
    if(zahl2 < zahl1):
        print(zahl2)
    if(zahl1 < zahl2):
        print (zahl1)
    if(zahl1 > zahl2):
        print(zahl1)
    if(zahl2 > zahl1):
        print(zahl2)