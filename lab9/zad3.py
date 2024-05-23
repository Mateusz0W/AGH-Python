#!/usr/bin/env python3.11
'''
aaa
'''
def leap_year(year):
    if (year%4==0 and year %100 !=0) and year%400 ==0:
        return True
def  correct_date(day,month,year):
    if month<=7:
        if month % 2==1:
            if 0>day>31:
                raise ValueError
        elif month==2 and leap_year(year):
            if 0>day>29:
                raise ValueError
        elif month==2 and not leap_year(year):
            if 0>day>28:
                raise ValueError
        else:
            if 0>day>30:
                raise ValueError
    if 12>=month>7:
        if month % 2==0:
            if 0>day>31:
                raise ValueError
        else:
            if 0>day>30:
                raise ValueError

def age(date,today):
    age=int(today[2])-int(date[2])
    if(int(today[1])<int(date[1])):
        age-=1
    elif(int(today[1])==int(date[1])):
        if(int(today[0])<int(date[0])):
            age-=1
    return age

def average(file,strict_mode=True):
     with open(file, 'r') as f:
            dates = f.readlines()
            parts=[]
            for i in dates:
                if(len(i.strip().split())==3):
                    parts.append(i.strip().split())
            sum=0
            ave=0
            for i in range(len(parts)):
                if(strict_mode):
                    if(correct_date(int(parts[i][0]),int(parts[i][1]),int(parts[i][2]))==False):
                        raise ValueError
                today=['09','05','2024']
                sum+=age(parts[i],today)
                ave=sum//(i+1)
            return ave
print(__doc__)