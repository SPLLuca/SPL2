# uebung4.py
import random

zahlen = []
hallo = [".","..","...","....","....."]
anzahlwuerfe = int(input("Wie oft soll simuliert werden?"))
for i in range(0, anzahlwuerfe):
    wurf = (random.randint(1,37))
    zahlen.append(wurf)
    #print(wurf, end = hallo[random.randint(0,4)])

print()

for i in range(1,37):
    print (i,"er : ", zahlen.count(i))
