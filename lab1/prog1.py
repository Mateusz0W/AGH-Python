import math

print("Wprowadz liste")
lista=[]
suma=0

while True:
    value=input()
    if value=='q':
        break
    else:
        lista.append(int(value))
    
print("lista:",lista[:])
for element in lista:
    suma+=element
print("Suma wszystkich liczb:",suma)
print("Największa liczba:",max(lista))
print("Najmniejsza liczba:",min(lista))
print("Liczba elementów w liście:",len(lista))


