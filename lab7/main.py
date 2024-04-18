import random

#1
def Pascal():
    row =[1]
    while True:
        yield row
        row=[x + y for x, y in zip([0]+row, row+[0])]
g = Pascal()
for i in range(10):
	print(next(g))
#2
N=40
series=[random.randint(0,1) for _ in range(N)]

def gen(series):
    zero=0
    for i in series:
        if i ==1:
            yield zero
            zero=0
        else:
            zero+=1

for i in gen(series):
    print(i,end=' ')
print('')
#3
def Fib(n):
    a, b = 0, 1
    for i in range(n):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            a, b = b, a + b  
            yield b


for number in Fib(10):
    print(number, end=' ')
print('')

def f(seq,even=True):
    for i in seq:
        if even:
            if not i%2:
                yield i
        else:
            if i%2:
                yield i

seq=[1,2,3,4,5,6,7,8,9,10]

print(list(f(seq)))
print(list(f(seq,False)))

def f2(seq):

    for i in seq:
        if i==seq[0]:
            yield i
        if i > seq[1]:
            break
#4 
def Myrange(*params):
    if len(params)==1 and params[0]>0:
        start,stop,step= 0,params[0],1
    elif len(params)==2 and params[1]-params[0]>0:
        start,stop,step= params[0],params[1],1
    elif len(params)==3 and (params[1]-params[0]) *params[2]>0 and params[2]>0:
        start,stop,step= params[0],params[1],params[2]
    while(start<stop):
        yield start
        start+=step
print(list(Myrange(7)))
#5

def walk(N):
    steps_right=sum(random.choice[True,False] for _ in range(N))
    steps_left=N-steps_right
    yield 2*steps_right -N
    