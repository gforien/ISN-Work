# compréhension simple de liste
liste = [k for k in range(1000)]

# impossible d'utiliser une boucle while
# [random.randint(0, 100) while random.randint(0, 100) != 0]

# k n'est utilisé qu'en tant que compteur
liste = [random.randint(0, 100) for k in range(1000)]

# k n'est utilisé qu'en tant que résultat de test
liste = [k for k in range(100) if random.randint() != 0]

# n'importe quelle autre liste permet l'itération
liste = [k for k in dir(list)]

# utiliser une boucle avec une condition
liste = [k for k in dir(list) if '__' not in k]

# compréhension de liste réinjectée dans une autre
liste = [k/2 for k in [l**2 for l in range(0, 100)]]

# compréhension avec deux boucles itératives
# la boucle de l est imbriquée dans celle de k
liste = [(k*l) for k in range(10) for l in range(5)]

# de cette manière, on peut génerer des tuples
liste = [(k,l) for k in range(10) for l in range(5)]

# impossible d'avoir deux variables évoluant en meme temps, mais différemment
# [(k,l) for (k,l) in (range(1, 11, 1), range(2, 22, 2))]

# les compréhensions peuvent être utilisées comme une liste déjà créée
for i in [(k+l) for k in range(10) for l in range(5)]:
    print(i)

for i in len([(k+l) for k in range(10) for l in range(5)]):
    print([(k+l) for k in range(10) for l in range(5)][i])
