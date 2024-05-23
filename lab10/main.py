import math
import random
import matplotlib.pyplot as plt
#1
class IFS:
    def __init__(self,W,P):
        self.W=W
        self.P=P
        self.points=[(0,0)]
    def transformation(self,itterations):
        for _ in range(itterations):
            x,y=self.points[-1]
            index=random.choices(range(len(self.W)),self.P)[0]
            a,b,c,d,e,f=self.W[index]
            new_x=a*x+b*y+c
            new_y=d*x+e*y+f
            self.points.append((new_x,new_y))
    def draw(self):
        x,y=zip(*self.points)
        plt.scatter(x,y,s=0.1)
        plt.show()
transformations = [
    (0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065),
    (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236),
    (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)
]
probabilities = [0.9, 0.05, 0.05]
ifs = IFS(transformations, probabilities)
ifs.transformation(100000)
ifs.draw()

#2
class Vector3D:
    def __init__(self,x,y,z):
        self.__x=x
        self.__y=y
        self.__z=z
    def len(self):
       return math.sqrt(self.__x**2+self.__y**2+self.__z**2)
    def iloczyn_skalarny(self,other):
        return  self.__x*other.getX() +self.__y*other.getY()+self.__z*other.getZ()
    def iloczyn_wektorowy(self,other):
        x=self.__y*other.getZ() -self.__z*other.getY()
        y=self.__z*other.getX() -self.__x*other.getZ()
        z=self.__x*other.getY() -self.__y*other.getX()
        return Vector3D(x,y,z)
    def iloczyn_mieszany(self,vec1,vec2):
        iloczyn_wektrowy=self.iloczyn_wektorowy(vec1)
        return iloczyn_wektrowy.iloczyn_skalarny(vec2)
    def __add__(self,other):
        return Vector3D(self.__x+other.getX(),self.__y+other.getY(),self.__z+other.getZ())
    def __sub__(self,other):
        return Vector3D(self.__x-other.getX(),self.__y-other.getY(),self.__z-other.getZ())
    def __mul__(self,value):
        return Vector3D(self.__x*value,self.__y*value,self.__z*value)
    def __rmul__(self, value):
        return self.__mul__(value)
    def __str__(self):
        return f"wektor3D({self.__x},{self.__y},{self.__z})"
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getZ(self):
        return self.__z

#3
vec1=Vector3D(1,2,3)
vec2=Vector3D(3,2,1)
def strumień_idukcji_magnetycznej(B,S):
    return B.iloczyn_skalarny(S)
def Lorenz_Force(q,E,V,B):
    VxB=V.iloczyn_wektorowy(B)
    return q*(E+VxB)
def Lorenz_Work(q,E,V):
    return V.iloczyn_skalarny(q*E)
print(strumień_idukcji_magnetycznej(vec1,vec2))
print(Lorenz_Force(3,vec1,vec2,Vector3D(4,5,6)))
print(Lorenz_Work(3,vec1,vec2))
