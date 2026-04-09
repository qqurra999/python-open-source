import unittest
from lab6 import Library, Book, Member


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.b1 = Book("Wiedźmin", "Sapkowski", 1990, "111")
        self.m1 = Member("Jan", "M01")

        self.lib.add_book(self.b1)
        self.lib.register_member(self.m1)

    def test_borrow_success(self):
        wynik = self.lib.borrow("111", "M01")
        self.assertTrue(wynik)
        self.assertFalse(self.b1.dostepnosc)

    def test_borrow_fail_unavailable(self):
        self.lib.borrow("111", "M01")
        wynik = self.lib.borrow("111", "M01")
        self.assertFalse(wynik)

    def test_search(self):
        wyniki = self.lib.search_by_title("Wiedź")
        self.assertEqual(len(wyniki), 1)
        self.assertEqual(wyniki[0].isbn, "111")