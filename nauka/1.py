#metoda najmniejszych kwadratów
import math
Uh=[0.591, 0.584, 0.581,0.447, 0.445, 0.446,0.398, 0.396, 0.394,0.259, 0.258, 0.255]
v=[625*10**12,625*10**12,625*10**12, 600*10**12,600*10**12,600*10**12, 508.47*10**12,508.47*10**12,508.47*10**12, 476.19*10**12,476.19*10**12,476.19*10**12]

average_Uh=sum(Uh)/len(Uh)
average_v=sum(v)/len(v)
D=0
for i in v:
    D+=(i-average_v)**2
sum1=0
for i in range(len(v)):
    sum1+=Uh[i]*(v[i]-average_v)
a=sum1/D
b=average_Uh-a*average_v
sum3=0
for i in range(len(v)):
    sum3+=(Uh[i]-(a*v[i]+b))**2
Sy=math.sqrt(sum3/(len(Uh)-2))
ua=Sy/math.sqrt(D)
ub=Sy*math.sqrt(1/len(v)+average_v**2/D)
print(D)
print(Sy)
print(a,b)
print(ua,ub)