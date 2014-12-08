#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as t

class Fenetre(t.Tk):
    def __init__(self):
        t.Tk.__init__(self)

        self.label = t.Label(self, text="Hello World !")
        self.label.pack()

        self.bouton = t.Button(self, text="Quitter", command=self.quit)
        self.bouton.pack()

fen = Fenetre()
fen.mainloop()
