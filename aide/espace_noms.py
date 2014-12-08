###             Accès et mutations d'une variable, espaces de noms
# print(variable)  ->  accès
# variable = 0     ->  mutation


espacePrincipal = 0

def ma_fonc():
    espaceFonc = 0


def ma_fonc_acces():
#       accède à l'espace principal
    print(espacePrincipal)                                                              #  good
#       ne peut accéder à l'espace d'une fonction
    print(espaceFonc)                                                                   #  NameError


def ma_fonc_mute():
#       tente de modifier une variable de l'espace principal
    espacePrincipal += 1                                                                #  UnboundLocalError
#       tente de modifier une variable de l'espace d'une fonction
    espaceFonc += 1                                                                     #  UnboundLocalError


def ma_fonc_redef():
#       définit une nouvelle adresse mémoire
#   espacePrincipal (espace ma_fonc_redef) remplace espacePrincipal (espace principal)
    espacePrincipal = 0                                                                 # good


def ma_fonc_double():
#       ne s'exécute pas, la définition de variable est considerée comme juste
#       et l'accès à l'espace principal est consideré comme un accès à une variable
#       non-définie. elle ne peut combiner ces deux actions :
    print(espacePrincipal)                # espacePrincipal (espace principal)          # UnboundLocalError
    espacePrincipal = 0                   # espacePrincipal (espace ma_fonc_double)     # good


def mon_fonc_objet():
#       les méthodes d'un objet définies dans l'espace principal sont invocables
#       on pourrait essayer  de modifier un objet par une de ses méthodes
#       'real' est un attribut contenant la valeur d'un entier
#       on obtient : attribute 'real' of 'int' objects is not writable
    espacePrincipal.__setattr__('real', 0)                                              # AttributeError
    setattr(espacePrincipal, 'real', 0)                                                 # AttributeError
    object.__setattr__(espacePrincipal, 'real', 0)                                      # AttributeError
