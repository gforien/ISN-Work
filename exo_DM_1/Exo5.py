#!/usr/bin/python3
# -*-coding:utf-8 -*

def taux_acc(f, a):
    return (f(a+0.0000000001)-f(a))//0.0000000001
