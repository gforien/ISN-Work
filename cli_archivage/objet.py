#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Fichier_a_archiver():
    def __init__(self):
        self.nom = ''
        self.fichiers = []
        self.taille = 0
        self.taille_str = ''

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
            self.taille_str = str(int(self.taille))
        except ValueError:
            self.taille_str = '0'
#       si la taille est un entier en Ko, Mo, Go...
        if len(self.taille_str)%3 != 0:
            puissance = len(self.taille_str)//3
            self.taille_str = self.taille_str[:len(self.taille_str)%3]
#       si la taille est un flottant en Ko, Mo, Go...
        else:
            puissance = len(self.taille_str[1:])//3
            self.taille_str = self.taille_str[:3]
        self.taille_str += ' '+taille_str_dic[1000**puissance]

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
