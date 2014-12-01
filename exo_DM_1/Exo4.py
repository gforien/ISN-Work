#!/usr/bin/python3
# -*-coding:utf-8 -*

def fact(n):
    fact_n = 1
    try:
        n = int(n)
    except (ValueError, TypeError):
        n = 0
    for i in range(1, n+1):
        fact_n *= i
    return fact_n

def p_parmi_n(p, n):
    p_parmi_n = 0
    try:
        p = int(p)
        n = int(n)
    except (ValueError, TypeError):
        p = 0
        n = 0
    p_parmi_n = fact(n)// fact(p) // fact(n-p)
    return p_parmi_n


if __name__ == "__main__":
    print("Quel calcul voulez-vous faire ?")
    print("1. n!")
    print("2. coefficient binomial (n p) : \"p parmi n\"")
    while 1:
        try:
            choice = int(input("Choix : "))
            assert choice == 1 or choice == 2
        except (ValueError, TypeError, AssertionError):
            pass
        else:
            break

    if choice == 1:
        n = input("Entrez n pour obtenir n! : ")
        print(n+"! = "+str(fact(n)))
    elif choice == 2:
        p = input("Entrez p : ")
        n = input("Entrez n : ")
        print(p,"parmi",n, "=", p_parmi_n(p,n))
