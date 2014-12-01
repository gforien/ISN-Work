#!/usr/bin/python3
# -*-coding:utf-8 -*

moyenne = float(input("Veuillez entrer la moyenne que vous avez obtenu au premier tour du baccalauréat : "))
print ("Résultat :\n")

if moyenne < 8.0:
    print("Recalé")
elif moyenne >= 8.0 and moyenne < 10.0:
    print("Admis au second tour")
elif moyenne >= 10.0:
    print("Admis")
    if moyenne >= 12.0 and moyenne < 14.0:
        print("Mention : Assez Bien")
    if moyenne >= 14.0 and moyenne < 16.0:
        print("Mention : Bien")
    elif moyenne >= 16.0:
        print("Mention : Très Bien")
