import unittest

from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Osman","12345")
        Number = phonebook.lookup("Osman")

        self.assertEqual('12345', Number)

