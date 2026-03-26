def silnia_iter(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik


def silnia_rek(n):
    if n <= 1:
        return 1
    return n * silnia_rek(n - 1)


def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print(f"Silnia (iter): {silnia_iter(5)}")
    print(f"Silnia (rek): {silnia_rek(5)}")
    print(f"NWD(48, 18): {nwd(48, 18)}")
    print(f"Czy 7 jest pierwsza?: {czy_pierwsza(7)}")

    print(f"Fibonacci (5 wyrazów): {list(fibonacci(5))}")
