###             Entrée controlée d'un nombre dans un programme console


##          avec break
val=0

while 1:
    try:
        val = int(input("Entrez un nombre entier entre 1 et 10: "))
        assert val >= 0 and val <= 10
    except AssertionError:
        print("Valeur absurde")
    except ValueError:
        print("Réessayez")
    else:
        break



##          avec un booléen
val=0
check=False

while not check:
    try:
        val = int(input("Entrez un nombre entier entre 1 et 10: "))
        assert val >= 0 and val <= 10
    except AssertionError:
        print("Valeur absurde")
    except ValueError:
        print("Réessayez")
    else:
        check = True
