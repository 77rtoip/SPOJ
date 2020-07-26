# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 11:27:44 2020

@author: ozon7

https://pl.spoj.com/problems/CHAOS/

Wejście
W pierwszej linijce standardowego wejścia znajduje się dokładnie jedna
liczba całkowita n - liczba prób Wolfganga upieczenia jego ciasta.
W kolejnych n liniach otrzymasz godzinę w formacie "GG:MM", wskazującą obecną godzinę
w formacie 24-godzinnym (Więc 0 <= GG <= 23 oraz 0 <= MM <=59 i godzina "00:00" następuje
po godzinie "23:59").

Wyjście
Dla każdego przypadku na wyjściu powinna pojawić się godzina w formacie "GG:MM".
UWAGA: Sprawdzając czy godzina jest palindromem nie bierzemy pod uwag wiodących zer
liczby GG, a w przpadku gdy GG = 0, wtedy nie bierzemy również pod uwagę
zer wiodących liczby MM.
"""

class Hour:
    def __init__(self, a : str):
        self.h, self.m = map(int, a.split(':'))

    def __repr__(self):
        return str(self.h).zfill(2) + ':' + str(self.m).zfill(2)

    def add_minute(self):
        self.m += 1
        if self.m >= 60:
            self.m %= self.m;
            self.h = (self.h + 1) % 24

    def to_int(self):
        return int(str(self.h) + str(self.m).zfill(2))

def ispalindrome(n):
    s = str(n)
    return s == s[::-1]


input_lines_count = int(input())

while input_lines_count:
    h = Hour(input())
    while True:
        h.add_minute()
        if ispalindrome(h.to_int()):
            print(h)
            break
    input_lines_count -= 1

