def silnia_iteracyjna(n):
    """Oblicza silnię liczby n przy użyciu pętli."""
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik


def silnia_rekurencyjna(n):
    """Oblicza silnię liczby n wywołując samą siebie."""
    if n == 0 or n == 1:
        return 1
    return n * silnia_rekurencyjna(n - 1)


def nwd(a, b):
    """Znajduje największy wspólny dzielnik algorytmem Euklidesa."""
    while b:
        a, b = b, a % b
    return a


def czy_pierwsza(n):
    """Sprawdza, czy liczba n jest liczbą pierwszą."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generator_fibonacci(n):
    """Generuje n pierwszych wyrazów ciągu Fibonacciego."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Przykład użycia:
if __name__ == "__main__":
    print(f"Silnia (it): {silnia_iteracyjna(5)}")
    print(f"Silnia (rek): {silnia_rekurencyjna(5)}")
    print(f"NWD(48, 18): {nwd(48, 18)}")
    print(f"Czy 7 jest pierwsza?: {czy_pierwsza(7)}")
    print("Fibonacci (5 wyrazów):", list(generator_fibonacci(5)))