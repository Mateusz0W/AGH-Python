import random
import sys
import string

#1
def zad1(s):
	constants = string.ascii_letters.replace('x', '')
	random_values = ''.join([str(random.randrange(10)) for _ in range(len(constants))])
	tr = str.maketrans(constants, random_values)
	return [(x := random.random(), eval(s.translate(tr))) for _ in range(10)]

print(zad1(sys.argv[1]))


#2
lista=[]
def zad2(*args):
    for i in args[0]:
        if all(i in j for j in args[1:]):
            lista.append(i)
    else:
        pass
    return lista
zad2([1,2,3], (1,3,5), [3,2])
print(lista)
lista.clear()
zad2([1,2,3], (1,3,5), [3,2,1])
print(lista)

#3
def zad3(lista1,lista2,stan=True):
    if stan:
        lista3=[(lista1[i],lista2[i]) for i in range (min(len(lista1),len(lista2)))]
    else:
        lista3=[(lista1[i] if i <len(lista1) else None,lista2[i] if i <len(lista2) else None) for i in range(max(len(lista1),len(lista2)))]
    return lista3
print(zad3([1,2,3],[1,2,4,5]))
print(zad3([1,2,3],[1,2,4,5],False))
#4
def zad4(amount,nominals=(10,5,2)):
    i=0
    nominal=nominals[i]
    change=[]
    while amount>0:
        if amount -nominal <0:
            i+=1
            if i < len(nominals): 
                nominal = nominals[i]
            else:
                break  
        change.append(nominal)
        amount -= nominal
    return change
print(zad4(58))

#5
def zad5(value,min,max,method='r'):
    steps=0
    while min<=max:
        steps +=1
        guess=random.randint(min,max) if method =='r' else (min +max )//2
        if guess == value:
            return steps
        elif guess <value:
            min+=1
        else:
            max-1
    return steps
print(zad5(5,0,20))
print(zad5(5,0,20,'b'))
        

