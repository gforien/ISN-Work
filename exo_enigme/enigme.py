#!/usr/bin/python3
# -*-coding:utf-8 -*

"""Programme donnant un tableau de solutions à l'adaptation de cette énigme :
"Utilisez tous les chiffres allant de 0 à 9 et les signes + - / * pour former un nombre égal à 42"
On entrera n'importe quel nombre et un tableau contenant toutes les expressions égales à ce nombre seront renvoyées."""

def entree():
    essais = 5
    while essais:
        try:
            result = int(input("Entrez le nombre: "))
        except (ValueError, TypeError):
            essais -= 1
        else:
            essais = 0
        if essais == 1:
            print("Valeur prise par défaut : 42")
            result = 42
            essais = 0
    return result


def init_tab():
    chaine = '0123456789+-*/'
    tableau = []
    for i in range(LONGUEUR):
        tableau.append(chaine[i])
    return tableau


def incre_index(index, verif):
    index[-1] += 1
    for i in range(LONGUEUR-1, -1, -1):
        if i != 0 and index[i] == LONGUEUR: # la chaine contient 14 valeurs
            index[i-1] += 1
            index[i] = 0
        if i == 0 and index[i] == LONGUEUR:
            verif = False
    return (index,verif)


def tri(expression):
    position = 0
    caractere = ''
    for i in range(LONGUEUR):
# aucun signe au début ou à la fin
        if expression[0] in '+*/' or expression[LONGUEUR-1] in '+-*/':
            return False
# aucuns signes se suivant
        if expression[i]+expression[i-1] in '+-*/':
            return False
# aucuns caractères identiques
        position = i
        caractere = expression[i]
        for j in range(LONGUEUR):
            if j != position and expression[i] == caractere:
                return False
    return True


def egale(expression, resultat):
    nombres = []
    positions = []
#    for i in range(LONGUEUR):
#        if len(nombres):
#            if expression[i] in '+-*/':
#                nombres.append(expression[:i])
#                positions.append(i+1)
#        else:
#            if expression[i] in '+-*/':
#                nombres.append(expression[positions[len(nombres]-1:i])
    return True




LONGUEUR = 14
# la chaine des caractères possibles de l'expression en contient 14
result = entree()
tab = ['0', '1', '2', '3', '4', '5', '6', 7'', '8', '9', '+', '-', 'x', '%']
idx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
expre = ""
solutions = []
check = True
while check:
    expre = ""
    for i in range(LONGUEUR):
        expre += tab[idx[i]]
    print('EXPRE:', expre)
    if tri(expre) and egale(expre, result):
        solutions.append(expre)
        check = int(input("Voulez-vous continuer (1/0) ? "))
    (idx, check) = incre_index(idx, check)
print(solutions)
