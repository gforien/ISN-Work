#!/usr/bin/python3
# -*- coding: utf-8 -*-

class NombreBinaire:
    """Classe définissant un nombre binaire, c'est à dire un nombre de base 2"""

    def from_dec(self, nombreRecu):
        """Recoit en paramètre un nombre entier postif et modifie self.binaire et self.decimal en conséquence"""
        self.binaire = str()
        self.decimal = int()
        binaireInverse = list()

        # vérifie que nombreRecu est un int positif, sinon lui affecte 0
        try:
            assert int(nombreRecu) == nombreRecu and nombreRecu >= 0
        except (ValueError, TypeError, AssertionError):
            nombreRecu = int(0)
        finally:
            self.decimal = nombreRecu    
        # conversion : la liste se remplit avec les restes des divisions (entières)  successives du nombre décimal
        i = -1
        while 1:
            i += 1    
            binaireInverse.append(self.decimal % 2)
            self.decimal //= 2
            if self.decimal == 0:
                break
    
        # le nombre binaire obtenu dans la liste est inversé, il doit être lu à l'envers,
        #  on le tranforme donc en chaine de caractères
        # la valeur de i doit être conservée entre ces deux boucles, c'est le nombre de chiffres
        for j in range(i+1):
            self.binaire += str(binaireInverse[i])
            i -= 1
        self.decimal = nombreRecu
        self.binaire = int(self.binaire)                            # on transforme la chaine en entier pour retourner un int

    def from_bin(self, nombreRecu):
        """Recoit en paramètre un nombre binaire et modifie self.binaire et self.decimal en conséquence"""
        self.binaire = list()
        self.decimal = 0
        erreurNombre = False
        j = -1
        k = 0
        nombreRecu = str(nombreRecu)

        # vérifie que nombreRecu est un int binaire, sinon lui affecte 0
        for i in nombreRecu:
            if not(i in "01"):
                erreurNombre = True
            else:
                j += 1
                self.binaire.append(int(i))
        if not(erreurNombre):
            for k in self.binaire:
                self.decimal += k*(2**j)
                j -= 1
            self.binaire = int(nombreRecu)
        else:
            self.binaire = 0
            self.decimal = 0
