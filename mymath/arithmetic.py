def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a