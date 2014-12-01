#!/usr/bin/python3.2
# -*- coding: utf-8 -*-

try:
    import zlib
    import zipfile as zf
    import os
except erreurr as ImportError:
    exit(erreur)

###################################################################################################

present = """
-------------------------------------
|            archivage.py           |
-------------------------------------

Quelle action voulez-vous effectuer ?
    1. Créer une archive de fichiers
    2. Ajouter des fichiers à une archive existante
    3. Extraire les fichiers d'une archive
    4. Obtenir des informations sur une archive
    5. Quitter
"""
info_arc="""
Création: {}
Système d'origine: {}"""
info_ele="""
{}
            Taille originale: {}
            Taux de compression: {}"""
oui = ['o','oui','O','Oui','OUI']
non = ['n','non','N','Non','NON']
systeme = { 0 : 'Windows',
            3 : 'UNIX/Linux' }
taille_dic = { 1: 'o',
               1000: 'Ko',
               1000000: 'Mo',
               1000000000: 'Go',
               1000000000000: 'To'}
mois = { 1 : 'Janvier',
         2 : 'Février',
         3 : 'Mars',
         4 : 'Avril',
         5 : 'Mai',
         6 : 'Juin',
         7 : 'Juillet',
         8 : 'Août',
         9 : 'Septembre',
        10 : 'Octobre',
        11 : 'Novembre',
        12 : 'Décembre' }
i = 0
choix = 0
nom = ''
fichiers = []
suppr = []

###################################################################################################

def recuperer_fichiers(liste_fichiers):
    i = 0
    j = 0
    fichiers = []
    for i in range(len(liste_fichiers)):
        if liste_fichiers[i] == ',' and liste_fichiers[i-1] != '\\':
            fichiers.append(liste_fichiers[j:i])
            j = i+1
    fichiers.append(liste_fichiers[j:len(liste_fichiers)])
    for i in range(len(fichiers)):
        fichiers[i] = fichiers[i].strip()
    return fichiers

def couper_taille(taille):
    puissance = 1
    try:
        taille = str(int(taille))
    except ValueError:
        taille = '0'
    if len(taille)%3 != 0:
        puissance = len(taille)//3
        puissance = 1000**puissance
        taille = taille[:len(taille)%3]
    else:
        puissance = len(taille[1:])//3
        puissance = 1000**puissance
        taille = taille[:3]
    return taille+' '+taille_dic[puissance]

def archiver(fichiers, nom):
    archive = zf.ZipFile(nom, mode='w')
    for i in fichiers:
        archive.write(i, compress_type=zf.ZIP_DEFLATED)
    archive.close

def ajout_archive(fichiers, nom):
    archive = zf.ZipFile(nom, mode='a')
    for i in fichiers:
        archive.write(i, compress_type=zf.ZIP_DEFLATED)
    archive.close

def desarchiver(archive):
    nom_fichier = ''
    archive = zf.ZipFile(nom, mode='r')
    for nom_fichier in archive.namelist():
        fichier = open(nom_fichier, 'wb')
        fichier.write(archive.read(nom_fichier))
        fichier.close
        print(nom_fichier, 'extrait.')

def info_archive(archive):
    taille = ''
    pourcent = ''
    archive = zf.ZipFile(nom, mode='r')
    e = archive.getinfo(archive.namelist()[0])
    date = str(e.date_time[2])+' '+mois[e.date_time[1]]+' '+str(e.date_time[0])+'   '+str(e.date_time[3])+':'+str(e.date_time[4])
    print()
    print(nom.upper().center(60))
    print(info_arc.format(date, systeme[e.create_system]))
    for e in archive.infolist():
        taille = couper_taille(e.file_size)
        pourcent = str(e.compress_size*100/e.file_size)
        if len(pourcent) > 4:
            pourcent = pourcent[:4]
        pourcent += '%'
        print (info_ele.format(e.filename, taille, pourcent))

###################################################################################################

if __name__ == '__main__':

##  récupère le choix de l'utilisateur
    print(present)
    for i in range(3):
        try:
            choix = int(input("Votre choix: "))
            assert choix in [1, 2, 3, 4, 5]
        except (TypeError, ValueError):
            print("Entrez le nombre correspondant à votre choix.")
        except AssertionError:
            print("Ce choix n'existe pas.")
        else:
            break

##  archive des fichiers
    if choix == 1:
###     affectation du nom de l'archive
        nom = input("Entrez NOM de l'archive (qui sera alors nommée NOM.zip): ")
        if nom != "":
            nom += ".zip"
        else :
            nom = "nom.zip"

###     transforme la chaine recue en un tableau de valeurs
        fichiers = recuperer_fichiers(input("Entrez les noms de fichiers (fichier, fichier avec espaces, fichier\,avec\,virgules ...)\nFichiers: "))

###     supprime les fichiers non-existants de la liste
        for i in fichiers:
            if not os.path.isfile(i):
                suppr.append(i)
        for i in suppr:
            fichiers.remove(i)

        archiver(fichiers, nom)
###     supprime les fichiers après leur archivage
        for i in fichiers:
            os.remove(i)
        info_archive(nom)

##  ajoute des fichiers à une archive
    elif choix == 2:
        nom = input("Entrez le chemin vers l'archive: ")
        if is_zipfile(nom):
            fichiers = recuperer_fichiers(input("Entrez les noms de fichiers (fichier, fichier avec espaces, fichier\,avec\,virgules ...)\nFichiers: "))
            ajout_archive(fichiers, nom)
            for i in fichiers:
                os.remove(i)
            info_archive(nom)
        else:
            print("Fichier zip non trouvé !")

##  extrait des fichiers d'une archive
    elif choix == 3:
        nom = input("Entrez le chemin vers l'archive: ")
        if is_zipfile(nom):
            desarchiver(nom)
            os.remove(nom)
        else:
            print("Fichier zip non trouvé !")

##  affiche des informations sur une archive
    elif choix == 4:
        nom = input("Entrez le chemin vers l'archive: ")
        if is_zipfile(nom):
            info_archive(nom)
        else:
            print("Fichier zip non trouvé !")
