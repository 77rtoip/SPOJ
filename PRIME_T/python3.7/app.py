"""
PRIME_T - Liczby Pierwsze

https://pl.spoj.com/problems/PRIME_T/

Sprawdź, które spośród danych liczb są liczbami pierwszymi

Input
n - liczba testów n<100000, w kolejnych liniach n liczb z przedziału [1..10000]

Output
Dla każdej liczby słowo TAK, jeśli liczba ta jest pierwsza, słowo: NIE, w przeciwnym wypadku.

Example
Input:
3
11
1
4

Output:
TAK
NIE
NIE
"""

def isprime(n):
    if (n == 2) or (n == 3):
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

input_lines_count = int(input())

while input_lines_count:
    print(['NIE', 'TAK'][isprime(int(input()))])
    input_lines_count -= 1
