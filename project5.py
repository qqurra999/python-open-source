import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(message)s')
plik = Path('wydatki.json')


def wczytaj():
    if not plik.exists():
        logging.warning("Brak pliku.")
        return []
    try:
        with plik.open('r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        logging.error("Zły format pliku.")
        return []


def zapisz(dane):
    with plik.open('w', encoding='utf-8') as f:
        json.dump(dane, f, indent=2)


def dodaj(dane):
    kategoria = input("Kategoria: ")
    try:
        kwota = float(input("Kwota: "))
    except ValueError:
        logging.error("Błędna kwota.")
        return
    opis = input("Opis: ")

    dane.append({"kategoria": kategoria, "kwota": kwota, "opis": opis})
    zapisz(dane)
    logging.info("Dodano wydatek.")


def wyswietl(dane):
    for w in dane:
        logging.info(f"{w['kategoria']}: {w['kwota']} - {w['opis']}")


def suma(dane):
    wynik = {}
    for w in dane:
        k = w['kategoria']
        wynik[k] = wynik.get(k, 0) + w['kwota']

    for k, v in wynik.items():
        logging.info(f"{k}: {v}")


def main():
    dane = wczytaj()
    while True:
        logging.info("\n1. Dodaj | 2. Pokaż | 3. Suma | 4. Wyjście")
        wybor = input("Wybór: ")

        if wybor == '1':
            dodaj(dane)
        elif wybor == '2':
            wyswietl(dane)
        elif wybor == '3':
            suma(dane)
        elif wybor == '4':
            break
        else:
            logging.error("Błędny wybór.")


if __name__ == "__main__":
    main()