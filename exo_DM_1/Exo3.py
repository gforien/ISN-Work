#!/usr/bin/python3
# -*-coding:utf-8 -*

import random

print("Début des tirages :")
a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)

while a+b+c < 12:
    print(a,"+",b,"+",c, "=" ,a+b+c, "est inférieur à 12")
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)

if a+b+c == 12:
    print(a,"+",b,"+",c, "=", a+b+c, "est égal à 12\nBravo !")
else:
    print(a,"+",b,"+",c, "=", a+b+c, "est supérieur à 12\nBravo !")
