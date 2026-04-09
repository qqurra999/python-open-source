from dataclasses import dataclass, field
from typing import List


@dataclass
class Book:
    tytul: str
    autor: str
    rok: int
    isbn: str
    dostepnosc: bool = True

    def __str__(self):
        status = "Dostępna" if self.dostepnosc else "Wypożyczona"
        return f"'{self.tytul}' - {self.autor} ({status})"

    def __repr__(self):
        return f"Book(tytul='{self.tytul}', autor='{self.autor}', rok={self.rok}, isbn='{self.isbn}', dostepnosc={self.dostepnosc})"


@dataclass
class EBook(Book):
    format_pliku: str = "pdf"

    def __str__(self):
        return f"'{self.tytul}' - {self.autor} [EBook: {self.format_pliku}]"

    def __repr__(self):
        return f"EBook(tytul='{self.tytul}', autor='{self.autor}', rok={self.rok}, isbn='{self.isbn}', dostepnosc={self.dostepnosc}, format_pliku='{self.format_pliku}')"


class Member:
    def __init__(self, imie: str, id_czlonka: str):
        self.imie = imie
        self.id = id_czlonka
        self.wypozyczone_ksiazki: List[Book] = []

    def __str__(self):
        return f"Czytelnik: {self.imie} (ID: {self.id}), Wypożyczone: {len(self.wypozyczone_ksiazki)}"

    def __repr__(self):
        return f"Member(imie='{self.imie}', id='{self.id}', wypozyczone={self.wypozyczone_ksiazki})"


class Library:
    def __init__(self):
        self.ksiazki: List[Book] = []
        self.czlonkowie: List[Member] = []

    def add_book(self, ksiazka: Book):
        self.ksiazki.append(ksiazka)

    def register_member(self, czlonek: Member):
        self.czlonkowie.append(czlonek)

    def borrow(self, isbn: str, id_czlonka: str):
        ksiazka = next((k for k in self.ksiazki if k.isbn == isbn), None)
        czlonek = next((c for c in self.czlonkowie if c.id == id_czlonka), None)

        if ksiazka and czlonek and ksiazka.dostepnosc:
            ksiazka.dostepnosc = False
            czlonek.wypozyczone_ksiazki.append(ksiazka)
            return True
        return False

    def return_book(self, isbn: str, id_czlonka: str):
        czlonek = next((c for c in self.czlonkowie if c.id == id_czlonka), None)
        if not czlonek:
            return False

        ksiazka = next((k for k in czlonek.wypozyczone_ksiazki if k.isbn == isbn), None)
        if ksiazka:
            ksiazka.dostepnosc = True
            czlonek.wypozyczone_ksiazki.remove(ksiazka)
            return True
        return False

    def search_by_title(self, tytul: str):
        return [k for k in self.ksiazki if tytul.lower() in k.tytul.lower()]

    def search_by_author(self, autor: str):
        return [k for k in self.ksiazki if autor.lower() in k.autor.lower()]

    def __str__(self):
        return f"Biblioteka: {len(self.ksiazki)} książek, {len(self.czlonkowie)} czytelników"

    def __repr__(self):
        return f"Library(ksiazki={self.ksiazki}, czlonkowie={self.czlonkowie})"