import unittest
from HW07_Swapnil_Morakhia import anagrams_dd,anagrams_cntr,anagram_lst,covers_alphabet, book_index

class TestContainer(unittest.TestCase):

    def test_anagram_lst(self):
        """This checks the anagramas_list"""
        self.assertEqual(anagram_lst("dormitory","dirtyroom"),True)
        self.assertEqual(anagram_lst("iceman","manice"),True)
        self.assertEqual(anagram_lst("And","dan"),True)
        self.assertEqual(anagram_lst("",""),True)
        self.assertEqual(anagram_lst("Orange","Mango"),False)

    def test_anagrams_dd(self):
        """This check the anagrams_dd"""
        self.assertEqual(anagrams_dd("dormitory","dirtyroom"),True)
        self.assertEqual(anagrams_dd("iceman","manice"),True)
        self.assertEqual(anagrams_dd("And","dAn"),True)
        self.assertEqual(anagrams_dd("And","man"),False)
        
    def test_anagrams_counter(self):
        """This test checks the anagrams by Counter method"""
        self.assertEqual(anagrams_cntr("dormitory","dirtyroom"),True)
        self.assertEqual(anagrams_cntr("iceman","manice"),True)
        self.assertEqual(anagrams_cntr("iceman","man"),False)
        self.assertEqual(anagrams_cntr("",""),True)

    def test_covers_alphabet(self):
        """This test checks the covers alphabet"""
        self.assertEqual(covers_alphabet("We promptly judged antique ivory buckles for the next prize"),True)
        self.assertEqual(covers_alphabet("“The quick, brown, fox; jumps over the lazy dog!”"),True)
        self.assertEqual(covers_alphabet("we had a bad day"),False)
        self.assertEqual(covers_alphabet(""),False)

    def test_book_index(self):
        """This checks the index of the book"""
        self.assertEqual(book_index([('how', 3), ('much', 3), ('wood', 3), ('how', 2), ('much', 1)]),[['how', [2, 3]], ['much', [1, 3]], ['wood', [3]]] )
        
if __name__ == "__main__":
    unittest.main(exit = False,verbosity = 2)
