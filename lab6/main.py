import random
import math
import time
import sys

#1
powt =1000
N =10000

def forStatement(N):
    result=[]
    for i in range(N):
        result.append(i)
        #result.append(i**2)
    return result
def  listComprehension(N):
    return [i for i in range(N)]
def mapFunction(N):
    return map(lambda x:x,range(N))
def generatorExpression(N):
    return (i for i in range(N))

def tester(f):
    start=time.time_ns()
    for _ in range(powt):
        f(N)
    end=time.time_ns()
    return start-end


print(sys.version)
test = (forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

#2
r=1
a=2
n=1000
def MonteCarlo(_):
    points=tuple(random.uniform(-r,r) for _ in range(2))
    return points[0]**2 + points[1]**2 <= r**2

inside_points=list(filter(MonteCarlo,range(n)))
k=len(inside_points)
pi=a**2 * k/n
print(pi)

#3 
x=list(random.uniform(-10,10) for _ in range (40))
y=list(random.uniform(-10,10) for _ in range (40))

def NajmniejszeKwadraty(x=[],y=[]):
    averageX=sum(x)/len(x)
    D = sum(map(lambda Xi: (Xi - averageX) ** 2, x))
    sum1 = sum(map(lambda Xi, Yi: (Yi * (Xi - averageX)), x, y))
    a=sum1/D
    averageY=sum(y)/len(y)
    b=averageY-a*averageX
    sum2 = sum(map(lambda Yi, Xi: (Yi - (a * Xi + b)) ** 2, y, x))
    Sy=math.sqrt(sum2/(len(x)-2))
    ux=Sy/math.sqrt(D)
    uy=Sy*math.sqrt(1/len(x)+averageX**2/D)
    return a,b ,ux,uy
print(NajmniejszeKwadraty(x,y))

#4
list1=[1,2,3,4,5]
def myreduce(f,s):
    result=s[0]
    for i in range(1,len(s)):
        result=f(result,s[i])
    return result
    
print(myreduce(lambda x,y:x+y ,list1))
print(myreduce(lambda x,y:x*y ,list1))

#5
matrix=[[1,2,3],[356,4,76],[-8,34,2]]

print(list(map(max,matrix)))
print(list(map(max,zip(*matrix))))
matrix1 = [[1, 2, 3], [356, 4, 76], [-8, 34, 2]]
matrix2 = [[10, 20, 30], [1, 2, 3], [4, 5, 6]]
print([list(map(sum, zip(*row_group))) for row_group in zip(matrix1, matrix2)])



