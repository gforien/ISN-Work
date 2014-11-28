#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

nombreDecimal = int()
nombreCopie = int()
nombreBinaireInverse = list()
nombreBinaire = str()

while 1:
    try:
        nombreDecimal = input("Entrez un nombre : ")
        nombreCopie = nombreDecimal = int(nombreDecimal)
    except (ValueError, TypeError):
        print("Veuillez entrer un nombre entier positif")
    except Exception as erreur:
        print("Une erreur est survenue : ", erreur)
    else:
        break

i = -1
print("Début des divisions successives :")
print("nombre : ", nombreDecimal,"\nbinaire = None")
while 1:
    i += 1    
    print("Tour n°", (i+1),":")
    print("\t\t", nombreCopie, " // 2 = ", (nombreCopie//2), "\t\t\t nombreBinaireInverse[",i,"] = ", (nombreCopie%2))
    nombreBinaireInverse.append(nombreCopie % 2)
    nombreCopie //= 2
    if nombreCopie == 0:
        break

print ("i = ", i)
for j in range(i+1):
    print("Tour n°", (i+1),":")
    nombreBinaire = nombreBinaire + str(nombreBinaireInverse[i])
    print("\t\t nombreBinaire = \"", nombreBinaire, "\"\t\t\t nombreBinaireInverse[",i,"] = ", nombreBinaireInverse[i], "\tj = ", j)
    i -= 1

print(nombreDecimal," base 10 = ", nombreBinaire," base 2")
