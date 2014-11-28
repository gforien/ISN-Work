#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
    from gi.repository import Gtk
except ImportError as importErreur:
    exit("La bibliothèque graphique Gtk n'a pu être importée :", importErreur)

class Fenetre(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Application GTK")
        self.resize(400,400)

        self.vBoite = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.bouton = Gtk.Button(label="Cliquez-moi")
        self.bouton.etat = 0
        self.bouton.connect("clicked", self.sur_bouton_clique)
        self.vBoite.pack_start(self.bouton, True, True, 0)

        self.label = Gtk.Label(label="")
        self.vBoite.pack_start(self.label, True, True, 0)

        self.add(self.vBoite)

    def sur_bouton_clique(self, widget):
        if widget.etat == 3:
            widget.etat = 1
        else:
            widget.etat += 1

        if widget.etat == 1:
            self.label.set_label("Hello")
        elif widget.etat == 2:
            self.label.set_label("World")
        if widget.etat == 3:
            self.label.set_label("!")


if __name__ == "__main__":
    fen = Fenetre()
    fen.connect("delete-event", Gtk.main_quit)
    fen.show_all()
    Gtk.main()
