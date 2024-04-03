#!/usr/bin/env python3.11

#chmod +x main.py


import random
import string

#1

k = 10
ls = [i for i in range(5*k)]
s = {}

for i in range(100):
        stable_elements = 0
        new_ls = ls[:]
        random.shuffle(ls)
        for j in range(k):
                if new_ls[j] == ls[j]:
                        stable_elements += 1
        if stable_elements in s:
                s[stable_elements] += 1
        else:
                s[stable_elements] = 1
print(s)
print('')

#2

lower_letters=''
sl=string.ascii_lowercase
for i in range(k):
    lower_letters+=sl[random.randrange(0,len(sl))]+'.'
print(lower_letters)
print('')
#3

#a
s2={}
lista=[random.randrange(0,20) for i in range(100)]

for i,j in enumerate(lista):
        s2.setdefault(j, []).append(i)
print(s2)

print('')

#b
s3={}

for i in lista:
    v=lista.index(i)
    s3.setdefault(i,[]).append(v)
print(s3)

print('')

#4
S4={}
Q=''
n=random.randint(3,6)
palindromes=0
for i in range(1000):
    for j in range(n):
        l=random.randrange(0,10)
        Q+=str(l)
    QR=Q[::-1]
    if Q==QR:
        palindromes+=1
    S4.setdefault(n,palindromes)
print(S4)
print('')
#5
A1={}
A2={}
for i in range(10):
    A1[i]=random.randrange(1,100)
    A2[i]=random.randrange(1,100)
A1 = {j: i for i,j in A1.items()}
A2 = {j: i for i,j in A2.items()}

A3 = {i: (A1[i], A2[i]) for i in A1 if i in A2}
print(A3)