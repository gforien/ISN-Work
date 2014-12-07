###             Gérer les arguments multiples avec listes et dictionnaires


##          récupération d'arguments multiples
def function(*positional, **keywords):
    for key, element in enumerate(positional):
        print("Positional argument n°{}: {}".format(key+1, element))
    for key, element in keywords.items():
        print("Keyword argument \"{}\": {}".format(key, element))

##          résultats:
""">>> function(12, 345, 'lala', 'lili')
       Positional argument n°1: 12
       Positional argument n°2: 345
       Positional argument n°3: 'lala'
       Positional argument n°4: 'lili'

\>>> function(123, arg='lalala', arg2='lilili', arg3='lololo')
     Positional argument n°1: 123
     Keyword argument "arg": lalala
     Keyword argument "arg2": lilili
     Keyword argument "arg3": lololo

\>>> function(arg='lalala', 123)
     SyntaxError: non-keyword arg after keyword arg"""


##          élargissement de liste ou de dictionnaire
##          pour passer plusieurs arguments au lieu d'un seul
liste = [12, 345, 'lili', 'lala']
dico = {"arg1": 123, "arg2": 456, "arg3": 890}
function(*liste, **dico)
