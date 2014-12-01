#!/usr/bin/python3
# -*-coding:utf-8 -*

nombre = int(input("Entrez un nombre n : "))
print()
i = 0
j = 0
chaine = ""
chaine_begin = 1
chaine_end = 1

if nombre%2 == 0:
    for i in range(1, nombre+1) : 
        print(i*str(i))

else:
    for i in range(nombre, 0, -1):
        if i == nombre:
            chaine_end = i+1

        chaine = ""

        for j in range(chaine_begin, chaine_end):
            chaine += str(j)
        chaine_begin += 1
        chaine_end -= 1

        if chaine != "":
            print(chaine)
