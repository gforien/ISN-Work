#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk

class Fenetre(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.resize(700, 700)

#       Définition des éléments de la fenêtre

##      tous les labels utilisés
        self.label = [Gtk.Label('Archiver'),
                      Gtk.Label('Réarchiver'),
                      Gtk.Label('Désarchiver'),
                      Gtk.Label('Info'),
                      Gtk.Label('Nom :'),
                      Gtk.Label('.zip'),
                      Gtk.Label('Fichiers :'),
                      Gtk.Label('Archivage :'),
                      Gtk.Label('Compression :')]
##      les champs d'entrée
        self.entry = [Gtk.Entry(), Gtk.Entry(), Gtk.Entry(), Gtk.Entry()]

##      les boutons radio
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


#       Création des boites

##      première boite, qui contient tout
        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

##      quatres sections horizontales
        masterBox = [Gtk.Box(), Gtk.Box(), Gtk.Box(), Gtk.Box()]
        mainBox.pack_start(masterBox[0], True, True, 0)
        mainBox.pack_start(masterBox[1], True, True, 0)
        mainBox.pack_start(masterBox[2], True, True, 0)
        mainBox.pack_start(masterBox[3], True, True, 0)

##      les troisième et quatrième sections contiennent 2 et 4 boites verticales
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


#       Inclusion des éléments dans les boites correspondantes

        self.add(mainBox)

        masterBox[0].pack_start(self.label[0], True, True, 0)
        masterBox[0].pack_start(self.label[1], True, True, 0)
        masterBox[0].pack_start(self.label[2], True, True, 0)
        masterBox[0].pack_start(self.label[3], True, True, 0)


        masterBox[1].pack_start(self.label[4], True, True, 0)
        masterBox[1].pack_start(self.entry[0], True, True, 0)
        masterBox[1].pack_start(self.label[5], True, True, 0)


        subBox[0].pack_start(self.label[6], True, True, 0)
        subBox[1].pack_start(self.entry[1], True, True, 0)
        subBox[1].pack_start(self.entry[2], True, True, 0)
        subBox[1].pack_start(self.entry[3], True, True, 0)


        subBox[2].pack_start(self.label[7], True, True, 0)
        subBox[3].pack_start(self.radio[0], True, True, 0)
        subBox[3].pack_start(self.radio[1], True, True, 0)
        subBox[4].pack_start(self.label[8], True, True, 0)
        subBox[5].pack_start(self.radio[2], True, True, 0)
        subBox[5].pack_start(self.radio[3], True, True, 0)
        subBox[5].pack_start(self.radio[4], True, True, 0)
        subBox[5].pack_start(self.radio[5], True, True, 0)
        subBox[5].pack_start(self.radio[6], True, True, 0)


    def pour_archivage_select(self, radio, choix):
        pass

    def pour_compression_select(self, radio, choix):
        pass




fen = Fenetre()
fen.connect('delete-event', Gtk.main_quit)
fen.show_all()
Gtk.main()
