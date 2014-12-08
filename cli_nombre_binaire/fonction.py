#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module contenant la fonction conversion_binaire()"""

def conversion_binaire(nombre):
    """Recoit en paramètre un nombre entier postif et le retourne en binaire"""

# vérification du type de nombre
    try:
        nombreDecimal = int(nombre)
        # vérifie que nombre est de type int ou float
        assert nombreDecimal >= 0 and int(nombre) == nombre
        # vérifie que nombre est un int positif
    except (ValueError, TypeError, AssertionError):
        # forceclose le programme si le paramètre donné ne correspond pas
        ## BRUTAL, à améliorer
        exit()

    nombreBinaireInverse = list()
    nombreBinaire = str()

# conversion : la liste se remplit avec les restes des divisions (entières),
#  successives du nombre
    i = -1
    while 1:
        i += 1    
        nombreBinaireInverse.append(nombreDecimal % 2)
        nombreDecimal //= 2
        if nombreDecimal == 0:
            break

# le nombre obtenu dans la liste est inversé, il doit être lu à l'envers,
#  on le tranforme donc en chaine de caractères
# la valeur de i doit être conservée entre ces deux boucles, c'est le nombre de chiffres
    for j in range(i+1):
        nombreBinaire = nombreBinaire + str(nombreBinaireInverse[i])
        i -= 1

# on transforme la chaine en entier pour retourner un nombre
    nombreBinaire = int(nombreBinaire)
    return nombreBinaire
