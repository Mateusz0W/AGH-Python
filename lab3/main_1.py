#!/usr/bin/env python3.11

#1
import sys

if (len(sys.argv) <= 1):
        print('Proszę uruchomić program z parametrami')
        sys.exit(-1)

st = ''.join(sys.argv[1:])
print(st)
print('')
#2
num=[]
lo=[]
up=[]
other=[]

for i in st:
    if i.isdigit():
        num.append(int(i))
    elif i.islower():
        lo.append(i)
    elif i.isupper():
        up.append(i)
    else:
        other.append(i)
print(num)
print(lo)
print(up)
print(other)
print('')

#3
newList=[]
for i in lo:
    if i  not in newList:
        newList.append(i)
List=[(i,lo.count(i)) for i in newList]
print(List)
print('')

#4

List.sort(key=lambda x:x[1])
print(List)
print('')

#5
a=0
b=0
L=[]
L.extend(lo)
L.extend(up)
samogloski='aeiyou'
for i in L:
    if i in samogloski:
        a+=1
    else:
        b+=1
Y=[(i,a*int(i)+b) for i in num]
print(Y)
print('')

#6
x = sum(i for i in num) / len(num)
y= sum(i for i in num) / len(num)

D = sum((i - x) ** 2 for i in num)
a = sum(j * (i - x) for i,j in Y) / D
b= y-a*x
print(x,' ',y,' ',D,' ',a,' ',b)