
liste = []
eingabe = ""
while (eingabe != "q"):
    eingabe = input("Geben Sie einen Text ein: ")
    if(eingabe != "q"):
        liste.append(eingabe)

liste.sort()
print(liste)