#!/usr/bin/python3
# -*-coding:utf-8 -*

import random

def coupe_baton_precis():
    longueur = 100
    coupe = [0,0,0]
    i = 0
    triangle = True
    
    coupe[0] = random.randint(1, (longueur-1))
    longueur -= coupe[0]
    if longueur < coupe[0]:
        longueur, coupe[0] = coupe[0], longueur
    
    coupe[1] = random.randint(1, (longueur-1))
    longueur -= coupe[1]
    coupe[2] = longueur
    
    for i in range(3):
        print("Le morceau", i+1,"a une longueur de",coupe[i])
    
    i = 0
    if coupe[i] > (coupe[i+1] + coupe[i-1]):
        triangle = False
        print(coupe[i+1],"+",coupe[i-1],"=",coupe[i+1]+coupe[i-1],"<",coupe[i])
        print("Les trois morceaux coupés ne permettent donc pas de faire un triangle.")
    elif triangle:
        print(coupe[i+1],"+",coupe[i-1],"=",coupe[i+1]+coupe[i-1],">",coupe[i])
    
    i = 1
    if coupe[i] > (coupe[i+1] + coupe[i-1]) and triangle:
        triangle = False
        print(coupe[i+1],"+",coupe[i-1],"=",coupe[i+1]+coupe[i-1],"<",coupe[i])
        print("Les trois morceaux coupés ne permettent donc pas de faire un triangle.")
    elif triangle:
        print(coupe[i+1],"+",coupe[i-1],"=",coupe[i+1]+coupe[i-1],">",coupe[i])
    
    i = 2
    if coupe[i] > (coupe[i-1] + coupe[i-2]) and triangle:
        triangle = False
        print(coupe[i-1],"+",coupe[i-2],"=",coupe[i-1]+coupe[i-2],"<",coupe[i])
        print("Les trois morceaux coupés ne permettent donc pas de faire un triangle.")
    elif triangle:
        print(coupe[i-1],"+",coupe[i-2],"=",coupe[i-1]+coupe[i-2],">",coupe[i])
    
    if triangle:
        print("Les trois morceaux coupés permettent bien de faire un triangle.")

    return triangle


def coupe_baton():
    longueur = 100
    coupe = [0,0,0, True]
    i = 0
    
    coupe[0] = random.randint(1, (longueur-1))
    longueur -= coupe[0]
    if longueur < coupe[0]:
        longueur, coupe[0] = coupe[0], longueur
    
    coupe[1] = random.randint(1, (longueur-1))
    longueur -= coupe[1]
    coupe[2] = longueur
    
    i = 0
    if coupe[i] > (coupe[i+1] + coupe[i-1]):
        coupe[3] = False
    
    i = 1
    if coupe[i] > (coupe[i+1] + coupe[i-1]) and coupe[3]:
        coupe[3] = False
    
    i = 2
    if coupe[i] > (coupe[i-1] + coupe[i-2]) and coupe[3]:
        coupe[3] = False

    return coupe
