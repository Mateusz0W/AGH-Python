#!/usr/bin/env python3.11

'''
Funckja Lunha przyjmuje argument number który jest stringiem
zwraca wartosc True jeśli numer karty jest poprawny
'''

def Luhna(number):
    card=[]
    if len(number)!=16:
        raise SyntaxError
    for i in range(len(number)):
        index=15-i
        if index %2 ==1:
            result=int(number[i]) *2
            if result >10:
                result=1 + (result%10)
                card.append(result)
        else:
            card.append(int(number[i]))
    val=sum(card)
    if val %10 != 0:
        raise ValueError



print(__doc__)