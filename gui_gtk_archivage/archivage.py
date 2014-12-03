#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
    import zlib
    import zipfile as zf
    from gi.repository import Gtk
    import os
except erreurr as ImportError:
    exit(erreur)


info_arc="{}".center(60)+\
"""Création: {}
Système d'origine: {}"""
info_ele="""{}
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



class Fenetre(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.resize(700, 700)

###             Définition des éléments de la fenêtre
##          boutons qui appellent les fonctions
        self.bouton = [Gtk.Button(label="Archiver"),
                       Gtk.Button(label="Réarchiver"),
                       Gtk.Button(label="Extraire"),
                       Gtk.Button(label="Info")]
        self.bouton[0].connect("clicked", self.appeler, 0)
        self.bouton[1].connect("clicked", self.appeler, 1)
        self.bouton[2].connect("clicked", self.appeler, 2)
        self.bouton[3].connect("clicked", self.appeler, 3)
##          tous les labels utilisés
        self.label = [Gtk.Label('Nom :'),
                      Gtk.Label('.zip'),
                      Gtk.Label('Fichiers :'),
                      Gtk.Label('Archivage :'),
                      Gtk.Label('Compression :')]
##          les champs d'entrée
        self.entry = [Gtk.Entry(), Gtk.Entry(), Gtk.Entry(), Gtk.Entry()]
##          les boutons radio
        self.radio = []
        self.radio.append(Gtk.RadioButton.new_from_widget(None))
        self.radio[0].set_label('.zip')
        self.radio[0].connect('toggled', self.pour_archivage_select, '.zip')
        self.radio.append(Gtk.RadioButton.new_from_widget(self.radio[0]))
        self.radio[1].set_label('.tar')
        self.radio[1].connect('toggled', self.pour_archivage_select, '.tar')
        self.radio.append(Gtk.RadioButton.new_from_widget(None))
        self.radio[2].set_label('None')
        self.radio[2].connect('toggled', self.pour_compression_select, 'None')
        self.radio.append(Gtk.RadioButton.new_from_widget(self.radio[2]))
        self.radio[3].set_label('.zip')
        self.radio[3].connect('toggled', self.pour_compression_select, '.zip')
        self.radio.append(Gtk.RadioButton.new_from_widget(self.radio[2]))
        self.radio[4].set_label('.bz2')
        self.radio[4].connect('toggled', self.pour_compression_select, '.bz2')
        self.radio.append(Gtk.RadioButton.new_from_widget(self.radio[2]))
        self.radio[5].set_label('.gz')
        self.radio[5].connect('toggled', self.pour_compression_select, '.gz')
        self.radio.append(Gtk.RadioButton.new_from_widget(self.radio[2]))
        self.radio[6].set_label('.xz')
        self.radio[6].connect('toggled', self.pour_compression_select, '.xz')

###             Création des boites
##          première boite, qui contient tout
        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
##          quatres sections horizontales
        masterBox = [Gtk.Box(), Gtk.Box(), Gtk.Box(), Gtk.Box()]
        mainBox.pack_start(masterBox[0], True, True, 0)
        mainBox.pack_start(masterBox[1], True, True, 0)
        mainBox.pack_start(masterBox[2], True, True, 0)
        mainBox.pack_start(masterBox[3], True, True, 0)
##          les troisième et quatrième sections contiennent 2 et 4 boites verticales
        subBox = [Gtk.Box(orientation=Gtk.Orientation.VERTICAL),
                  Gtk.Box(orientation=Gtk.Orientation.VERTICAL),
                  Gtk.Box(orientation=Gtk.Orientation.VERTICAL),
                  Gtk.Box(orientation=Gtk.Orientation.VERTICAL),
                  Gtk.Box(orientation=Gtk.Orientation.VERTICAL),
                  Gtk.Box(orientation=Gtk.Orientation.VERTICAL)]
        masterBox[2].pack_start(subBox[0], True, True, 0)
        masterBox[2].pack_start(subBox[1], True, True, 0)
        masterBox[3].pack_start(subBox[2], True, True, 0)
        masterBox[3].pack_start(subBox[3], True, True, 0)
        masterBox[3].pack_start(subBox[4], True, True, 0)
        masterBox[3].pack_start(subBox[5], True, True, 0)

#               Inclusion des éléments dans les boites correspondantes
        self.add(mainBox)
##          première section horizontale
        masterBox[0].pack_start(self.bouton[0], True, True, 0)
        masterBox[0].pack_start(self.bouton[1], True, True, 0)
        masterBox[0].pack_start(self.bouton[2], True, True, 0)
        masterBox[0].pack_start(self.bouton[3], True, True, 0)
##          deuxième section horizontale
        masterBox[1].pack_start(self.label[4], True, True, 0)
        masterBox[1].pack_start(self.entry[0], True, True, 0)
        masterBox[1].pack_start(self.label[5], True, True, 0)
##          troisième section horizontale
        subBox[0].pack_start(self.label[6], True, True, 0)
        subBox[1].pack_start(self.entry[1], True, True, 0)
        subBox[1].pack_start(self.entry[2], True, True, 0)
        subBox[1].pack_start(self.entry[3], True, True, 0)
##          quatrième section horizontale
        subBox[2].pack_start(self.label[7], True, True, 0)
        subBox[3].pack_start(self.radio[0], True, True, 0)
        subBox[3].pack_start(self.radio[1], True, True, 0)
        subBox[4].pack_start(self.label[8], True, True, 0)
        subBox[5].pack_start(self.radio[2], True, True, 0)
        subBox[5].pack_start(self.radio[3], True, True, 0)
        subBox[5].pack_start(self.radio[4], True, True, 0)
        subBox[5].pack_start(self.radio[5], True, True, 0)
        subBox[5].pack_start(self.radio[6], True, True, 0)


    def appeler(self, bouton, valeur):
        if choix == 1:
#            fichiers = recuperer_fichiers(input("Entrez les noms de fichiers (fichier, fichier avec espaces, fichier\,avec\,virgules ...)\nFichiers: "))
            for i in fichiers:
                if not os.path.isfile(i):
                    suppr.append(i)
            for i in suppr:
                fichiers.remove(i)
            archiver(fichiers, nom)
###         supprime les fichiers après leur archivage
            for i in fichiers:
                os.remove(i)
            info_archive(nom)

        elif choix == 2:
#            nom = input("Entrez le chemin vers l'archive: ")
            if is_zipfile(nom):
#                fichiers = recuperer_fichiers(input("Entrez les noms de fichiers (fichier, fichier avec espaces, fichier\,avec\,virgules ...)\nFichiers: "))
                ajout_archive(fichiers, nom)
                for i in fichiers:
                    os.remove(i)
                info_archive(nom)
        elif choix == 3:
#            nom = input("Entrez le chemin vers l'archive: ")
            if is_zipfile(nom):
                desarchiver(nom)
                os.remove(nom)
        elif choix == 4:
#            nom = input("Entrez le chemin vers l'archive: ")
            if is_zipfile(nom):
                info_archive(nom)

    def pour_archivage_select(self, radio, choix):
        pass

    def pour_compression_select(self, radio, choix):
        pass


if __name__ == '__main__':
    fen = Fenetre()
    fen.connect('delete-event', Gtk.main_quit)
    fen.show_all()
    Gtk.main()
