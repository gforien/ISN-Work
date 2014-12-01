#!/usr/bin/python3
# -*-coding:utf-8 -*

nombre = int(input("Entrez un nombre n : "))
print()
i = 0

if nombre%2 == 0:
    for i in range(nombre) : 
        print("1"+i*"0")
else:
    for i in range(nombre, 0, -2) : 
        print("1"+(i-1)*"0")
