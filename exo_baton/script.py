#!/usr/bin/python3
# -*-coding:utf-8 -*

try:
    from gi.repository import Gtk
    from coupe_baton import coupe_baton
except ImportError as importErreur:
    exit("La bibliothèque graphique Gtk ou un module nécessaire n'ont pu être importés :", importErreur)

class Fenetre(Gtk.Window):
    def __init__(self):
        i = 0
        Gtk.Window.__init__(self, title="Exercice du Bâton")
        self.resize(750,170)

        boite = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(boite)

        self.label = Gtk.Label(label="Cliquez pour commencer l'expérience")
        boite.pack_start(self.label, True, False, 0)

        hBoite = Gtk.Box()
        boite.pack_start(hBoite, True, True, 0)

        vBoite = []
        self.resultats = []
        self.ascii_art = []
        for i in range(3):
            vBoite.append(Gtk.Box(orientation=Gtk.Orientation.VERTICAL))
            self.resultats.append(Gtk.Label())
            self.ascii_art.append(Gtk.Label())
            vBoite[i].pack_start(self.resultats[i], True, False, 0)
            vBoite[i].pack_start(self.ascii_art[i], True, False, 0)
            hBoite.pack_start(vBoite[i], True, True, 0)

        self.bouton = Gtk.Button(label="Cliquez-moi")
        self.bouton.connect("clicked", self.execute)
        boite.pack_start(self.bouton, True, False, 0)

    def execute(self, widget):
        i = 0
        j = 0
        ascii_art = [str(), str(), str()]
        baton = coupe_baton()

        self.label.set_text("Longueur des bouts de bois :")

        for i in range(3):
            self.resultats[i].set_text(str(baton[i]))
            for j in range(baton[i]):
                ascii_art[i] += "-"
            self.ascii_art[i].set_text(ascii_art[i])

        if baton[3]:
            self.label.set_text(self.label.get_text() + "\nVous pouvez faire un triangle")
        else:
            self.label.set_text(self.label.get_text() + "\nVous ne pouvez pas faire de triangle")


if __name__ == "__main__":
    fen = Fenetre()
    fen.connect("delete-event", Gtk.main_quit)
    fen.show_all()
    Gtk.main()
