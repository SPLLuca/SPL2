# Zahlen einlesen

liste = []
eingabe = ""

while(eingabe!="-1"):
    eingabe = input("Geben Sie eine zahl ein:  ")
    if(eingabe!= "-1"):
        liste.append(int(eingabe))


print("ende")

liste.sort()
print(liste)