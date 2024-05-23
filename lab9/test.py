#!/usr/bin/env python3.11
import datetime
import zad1
import zad2
import zad3

try:
    zad1.Luhna('1234567891234563')
except SyntaxError:
    print('zakrótki numer karty')
except ValueError:
    print('bledny numer karty')
else:
    print('poprawny numer karty')

#2

birth= datetime.date(1902, 7, 8)
try:
    zad2.PESEL('02070803628',birth,'kobieta')
except KeyError:
    print('bledny miesioc')
except ValueError:
    print('bledny pesel')
except AttributeError:
    print('zla plec')
except BaseException:
    print('zla data')
else:
    print('poprawny numer pesel')

try:
    zad3.average(('daty.in'))
except ValueError:
    print('bledny data')