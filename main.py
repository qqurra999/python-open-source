from mymath.arithmetic import silnia, nwd
from mymath.sequences import czy_pierwsza, fibonacci
import requests

print(f"Silnia 5: {silnia(5)}")
print(f"NWD(48, 18): {nwd(48, 18)}")
print(f"Czy 7 pierwsza?: {czy_pierwsza(7)}")
print(f"Fibonacci: {list(fibonacci(5))}")
print(f"Version requests: {requests.__version__}")