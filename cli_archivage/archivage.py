#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import zipfile
import datetime

present = """
-------------------------------------
|            archivage.py           |
-------------------------------------

Quelle action voulez-vous effectuer ?
    1. Créer une archive de fichiers
    2. Ajouter des fichiers à une archive existante
    3. Récupérer les fichiers d'une archive
    4. Obtenir des informations sur une archive
"""
oui = ['o','oui','O','Oui','OUI']
non = ['n','non','N','Non','NON']
i = 0
j = 0
choix = 0
liste_fichier = ''
fichiers = []


def archiver(*fichiers):
#    cle = 0
#    for cle in range(len(fichiers)):
#        if zipfile.is_zipfile(fichiers[cle]) and not\
#(input(fichiers[cle]+" est un fichier zip existant : créer une nouvelle archive va l'effacer. Continuer ? ") in oui):
#            del fichiers[cle]
#    print(fichiers)
    pass

def ajout_archive():
    pass

def desarchiver():
    pass

def infos_archive():
    pass


print(present)
while 1:
    try:
        choix = int(input("Votre choix : "))
        assert choix in [1, 2, 3, 4]
    except (TypeError, ValueError):
        print("Entrez le nombre correspondant à votre choix.")
    except AssertionError:
        print("Ce choix n'existe pas")
    else:
        print()
        break

if choix == 1:
    liste_fichiers = input("Entrez les noms de fichiers (fichier, fichier avec espaces, fichier\,avec\,virgules ...)\nFichiers : ")

    for i in range(len(liste_fichiers)):
        if liste_fichiers[i] == ',' and liste_fichiers[i-1] != '\\':
            fichiers.append(liste_fichiers[j:i])
            j = i+1
    fichiers.append(liste_fichiers[j:len(liste_fichiers)])

    for i in range(len(fichiers)):
        fichiers[i] = fichiers[i].strip()

    archiver(*fichiers)

elif choix == 2:
    ajout_archive()


elif choix == 3:
    desarchiver()

else:
    infos_archive()
