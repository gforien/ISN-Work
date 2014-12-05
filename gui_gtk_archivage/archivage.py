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
        self.bouton[0].connect("clicked", self.archiver)
        self.bouton[1].connect("clicked", self.ajouter)
        self.bouton[2].connect("clicked", self.extraire)
        self.bouton[3].connect("clicked", self.info)
##          tous les labels utilisés
        self.label = [Gtk.Label('Nom :'),
                      Gtk.Label('.zip'),
                      Gtk.Label('Fichiers :'),
                      Gtk.Label('Archivage :'),
                      Gtk.Label('Compression :')]
##          les champs d'entrée
        self.entry = [Gtk.Entry(), Gtk.Entry()]
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
        masterBox[1].pack_start(self.label[0], True, True, 0)
        masterBox[1].pack_start(self.entry[0], True, True, 0)
        masterBox[1].pack_start(self.label[1], True, True, 0)
##          troisième section horizontale
        subBox[0].pack_start(self.label[2], True, True, 0)
        subBox[1].pack_start(self.entry[1], True, True, 0)
##          quatrième section horizontale
        subBox[2].pack_start(self.label[3], True, True, 0)
        subBox[3].pack_start(self.radio[0], True, True, 0)
        subBox[3].pack_start(self.radio[1], True, True, 0)
        subBox[4].pack_start(self.label[4], True, True, 0)
        subBox[5].pack_start(self.radio[2], True, True, 0)
        subBox[5].pack_start(self.radio[3], True, True, 0)
        subBox[5].pack_start(self.radio[4], True, True, 0)
        subBox[5].pack_start(self.radio[5], True, True, 0)
        subBox[5].pack_start(self.radio[6], True, True, 0)


###             Fonctions appelant l'objet fic de la classe FichierAArchiver
    def archiver(self, bouton):
        fichiers = self.entry[1].get_text()
        self.entry[1].set_text('')
        print(fichiers)
        fic.recuperer_fichiers(fichiers)
        fichiers = fic.fichiers
        print(fichiers)
#            for i in fichiers:
#                os.remove(i)
#            info_archive(nom)

    def ajouter(self, bouton):
#            if is_zipfile(nom):
#                ajout_archive(fichiers, nom)
#                for i in fichiers:
#                    os.remove(i)
#                info_archive(nom)
        pass
    def extraire(self, bouton):
#            if is_zipfile(nom):
#                desarchiver(nom)
#                os.remove(nom)
        pass
    def info(self, bouton):
#            if is_zipfile(nom):
#                info_archive(nom)

        pass
    def pour_archivage_select(self, radio, choix):
        pass
    def pour_compression_select(self, radio, choix):
        pass



class FichierAArchiver():
    def __init__(self):
        self.nom = ''
        self.fichiers = []
        self.taille = 0
        self.tailleChaine = ''

###             Fonctions non-spécifiques au format d'archivage
##          crée une liste de valeurs à partir de la chaine récupérée
##          et vérifie l'existence des fichiers
    def recuperer_fichiers(self, listeFichiers):
        i = 0
        j = 0
#       liste contenant les noms de fichiers à supprimer
        aSupprimer = []
        for i in range(len(listeFichiers)):
#       ajoute une entrée à fichiers[] si le caractère est une virgule non-échapée donc séparant deux noms
            if listeFichiers[i] == ',' and listeFichiers[i-1] != '\\':
                self.fichiers.append(listeFichiers[j:i].strip())
                j = i+1
#       ajoute la fin de la chaine au tableau
        self.fichiers.append(listeFichiers[j:len(listeFichiers)].strip())
#       ajoute le nom à la seconde liste si elle n'existe pas
        for i in range(len(self.fichiers)):
            if not os.path.isfile(self.fichiers[i]):
                aSupprimer.append(self.fichiers[i])
#       supprime les valeurs du tableau (en supprimant les clés, la liste s'ajusterait)
        for i in aSupprimer:
            self.fichiers.remove(i)

##          transforme un int de taille du fichier en une chaine de type "10 Mo"
    def couper_taille(self):
        puissance = 1
        try:
            self.tailleChaine = str(int(self.taille))
        except ValueError:
            self.tailleChaine = '0'
#       si la taille est un entier en Ko, Mo, Go...
        if len(self.tailleChaine)%3 != 0:
            puissance = len(self.tailleChaine)//3
            self.tailleChaine = self.tailleChaine[:len(self.tailleChaine)%3]
#       si la taille est un flottant en Ko, Mo, Go...
        else:
            puissance = len(self.tailleChaine[1:])//3
            self.tailleChaine = self.tailleChaine[:3]
        self.tailleChaine += ' '+tailleChaine_dic[1000**puissance]

###             ZIP
    def zip_archiver(self):
        archive = zf.ZipFile(self.nom, mode='w')
        for i in fichiers:
            archive.write(i, compress_type=zf.ZIP_DEFLATED)
        archive.close

    def zip_ajouter(self):
        archive = zf.ZipFile(self.nom, mode='a')
        for i in fichiers:
            archive.write(i, compress_type=zf.ZIP_DEFLATED)
        archive.close

    def zip_extraire(self):
        nom_fichier = ''
        archive = zf.ZipFile(self.nom, mode='r')
        for nom_fichier in archive.namelist():
            fichier = open(nom_fichier, 'wb')
            fichier.write(archive.read(nom_fichier))
            fichier.close

    def zip_info(self):
        message = ''
        taille = ''
        pourcent = ''
        archive = zf.ZipFile(self.nom, mode='r')

        element = archive.getinfo(archive.namelist()[0])
        date = str(element.date_time[2])+' '+mois[element.date_time[1]]+' '+str(element.date_time[0])+'   '+str(element.date_time[3])+':'+str(element.date_time[4])

#        message += nom.upper().center(60)+'\n'
        message += info_arc.format(nom, date, systeme[element.create_system])+'\n'
        for element in archive.infolist():
            taille = couper_taille(element.file_size)
            pourcent = str(element.compress_size*100/element.file_size)
            if len(pourcent) > 4:
                pourcent = pourcent[:4]
            pourcent += '%'
            message += info_ele.format(element.filename, taille, pourcent)+'\n'



if __name__ == '__main__':
    fic = FichierAArchiver()
    fen = Fenetre()
    fen.connect('delete-event', Gtk.main_quit)
    fen.show_all()
    Gtk.main()
