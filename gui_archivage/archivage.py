#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk

class Fenetre(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.resize(50, 70)

        boite = Gtk.Box()
        self.add(boite)

        self.champ = Gtk.Entry()
        boite.pack_start(self.champ, True, True, 0)

        bouton = Gtk.Button(label="Start")
        bouton.connect("clicked", self.pour_bouton_clique)
        boite.pack_start(bouton, True, True, 0)

    def pour_bouton_clique(self, bouton):
        self.archive(self.champ.get_text())
        self.champ.set_text("")

    def archive(self, fichier):
        print("LE FICHIER EST {}".format(fichier))

fen = Fenetre()
fen.connect("delete-event", Gtk.main_quit)
fen.show_all()
Gtk.main()
