import unittest

from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Osman","12345")
        Number = phonebook.lookup("Osman")
        self.assertEqual('12345', Number)
    
    # We are checking what happens if a name does not exist.
    # We want to be sure it raises a key error. If return code is True, means test is passed.
    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")
    
    #@unittest.skip('WIP')
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        
    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Anna","012345")
        self.assertTrue(self.phonebook.is_consistent())
        
    def test_is_consistent_with_duplicate_entries(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Anna","12345")
        self.assertFalse(self.phonebook.is_consistent())
        
    def test_is_consistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Anna","123")
        self.assertFalse(self.phonebook.is_consistent())
        
