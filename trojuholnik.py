"""
Trojuholnik.

Program si vyziada suradnice 3 bodov,
nasledne zisti dlzky stran, zostrojitelnost, pravouhlost, obvod a obsah
"""
import math
import sys


def vypocetStrany(x1, y1, x2, y2):
    """Vypocita vzdialenost dvoch bodov.

    >>> vypocetStrany(0, 0, 0, 2)
    2.0
    """
    strana = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return strana


def zostrojitelnost(a, b, c):
    """
    Zisti zostrojitelnost trojuholnika zo zadanych 3 stran.

    >>> zostrojitelnost(5, 6, 7)
    True
    """
    if((a+b > c) and (a+c) > b and (b+c) > a):
        return True
    else:
        return False


def pravouhlost(a, b, c):
    """
    Zisti pravouhlost trojuholnika zo zadanych troch stran.

    >>> pravouhlost(5, 8, 9)
    Nie je pravouhly
    """
    if((a > 0 and b > 0 and c > 0)
       and (a**2 == b**2+c**2 or b**2 == c**2+a**2 or c**2 == a**2+b**2)):
        print("Je pravouhly")
    else:
        print("Nie je pravouhly")


def obsah(a, b, c):
    """
    Vypocita obsah trojuholnika pomocou Heronovho vzorca.

    >>> obsah(4,9,8)
    15.998046755776157
    """
    if(zostrojitelnost(a, b, c)):
        p = (a + b + c) / 2
        obsah = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return obsah


def vstup():
    """
    Komunikacia s uzivatelom.

    Uzivatel ma na vyber vypocet alebo ukoncenie programu.
    V pripade volby vypoctu, program vyzve uzivatela,
    aby zadal suradnnice 3 bodov
    """
    while(True):
        vstup = input("Vypocitat trojuholnik [Y/N]: ")
        if(vstup == 'Y'):
            print("Zadaj suradnice 3 bodov: ")
            x1 = int(input("Zadaj x1: "))
            y1 = int(input("Zadaj y1: "))
            x2 = int(input("Zadaj x2: "))
            y2 = int(input("Zadaj y2: "))
            x3 = int(input("Zadaj x3: "))
            y3 = int(input("Zadaj y3: "))
            vypis(x1, y1, x2, y2, x3, y3)
        elif(vstup == 'N'):
            sys.exit()
        else:
            print("Zadaj Y alebo N")


def vypis(x1, y1, x2, y2, x3, y3):
    """
    Vypise vypocitane hodnoty a vlastnosti potencialneho trojuholnika.

    Dlzky stran, Zostrojitelnost, Obvod, Obsah, Pravouhlost
    """
    a = vypocetStrany(x1, y1, x2, y2)
    b = vypocetStrany(x2, y2, x3, y3)
    c = vypocetStrany(x3, y3, x1, y1)
    print("Dlzky stran: ")
    print("{:.2f}".format(a))
    print("{:.2f}".format(b))
    print("{:.2f}".format(c))
    if(zostrojitelnost(a, b, c)):
        print("Trojuholnik sa da zostrojit")
        obvod = a + b + c
        print("Obvod: ")
        print("{:.2f}".format(obvod))
        print("Obsah: ")
        print("{:.2f}".format(obsah(a, b, c)))
        pravouhlost(a, b, c)
    else:
        print("Trojuholnik sa neda zostrojit")


if __name__ == '__main__':
    vstup()
