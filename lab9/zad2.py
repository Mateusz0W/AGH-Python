#!/usr/bin/env python3.11
'''
Funckja PESEL przyjmuje argument pesel który jest stringiem date która pochodzi
z modułu datetime oraz gender ktora jest stringiem
funkcja sprawdza popwanosc numeru pesel
'''
def PESEL(pesel,date,gender):
    year=int(pesel[:2])
    month=int(pesel[2:4])
    day=int(pesel[4:6])
    sex=int(pesel[6:10])
    control=int(pesel[-1])
    if 80 < month <93:
        year=1800+year
        month-=80
    elif 0 >month<13:
        year=1900+year
    elif 20>month <33:
        year=2000+year
        month-=20
    elif 40>month <53:
        year=2100+year
        month-=40
    elif 60>month <73:
        year=2200+year
        month-=60
    else:
        raise KeyError
    if (sex %2 != 0 and gender=='kobieta') or (sex %2 != 1 and gender=='mężczyzna'):
        raise AttributeError
    d=str(year)+str(month)+'-'+str(day)
    if d != date:
        raise BaseException

    weights=[1,3,7,9,1,3,7,9,1,3]
    result=0
    for i in range(len(pesel)-1):
        result+=weights[i]*int(pesel[i])
    result%=10
    result=10-result
    result%=10
    if(result != control):
        raise ValueError

print(__doc__)