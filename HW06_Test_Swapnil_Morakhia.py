import unittest
from HW06_Swapnil_Morakhia import list_copy, list_intersect, list_difference, remove_vowels ,check_pwd, insertion_sort

class TestList(unittest.TestCase):

    def test_list_copy(self):
        """This checks the list copy method"""
        self.assertEqual(list_copy(["abc","def","mno","nnd"]),(["abc","def","mno","nnd"]))
        self.assertEqual(list_copy([""]),([""]))

    def test_list_intersect(self):
        """Ths checks the list intersect method"""
        self.assertEqual(list_intersect(["abc","def","xyx","gef"],["xyx","gef","lop","ben"]),["xyx","gef"])
        self.assertEqual(list_intersect(["abc","def","xyx","gef"],["mno","acv","lop","ben"]),[])

    def test_list_difference(self):
        """This checks the list difference method"""
        self.assertEqual(list_difference(["abc","def","xyx","gef"],["xyx","gef","lop","ben"]),["abc","def"])
        self.assertEqual(list_difference(["1","2","3","4"],["1","2","3","4"]),[])

    def test_remove_vowels(self):
        """This checks the remove vowels method"""
        self.assertEqual(remove_vowels("hello world"),"hll wrld")
        self.assertEqual(remove_vowels("why"),"why")
        self.assertEqual(remove_vowels("aeiou"),"")

    def test_check_password(self):
        """This checks the check_pwd method"""
        self.assertEqual(check_pwd("Swapnil24"),True)

    def test_insertion_sort(self):
        """This checks the insertion sort"""
        self.assertEqual(insertion_sort([1,5,3,3]),[1,3,3,5])
        self.assertEqual(insertion_sort([]),[])

if __name__ == "__main__":
    unittest.main(exit = False,verbosity = 2)
