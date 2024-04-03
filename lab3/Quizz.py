import math

k=[1,2,3,4,5,6]
for i in k:
    if i%2:
        print('break')
        break
else:
    print('else')

print(math.fabs(-2))

k[0],k[-1]=k[-2],k[1]
print(k)
print(type('a'))
print(1.//2.)
k=[1,2,3,4,5,6]
print(k[1:3])
k.append([1,2,3,4,5,6])
print(k)