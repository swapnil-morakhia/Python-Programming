from HW05_Swapnil_Morakhia import reverse, rev_enumerate, find_second, get_lines
import unittest 

class TestString(unittest.TestCase):

    def test_reverse(self):
        """This test checks the reverse of a string"""
        self.assertEqual(reverse("python"), "nohtyp")
        self.assertEqual(reverse("hello"), "olleh")

    def test_rev_enumerate(self):
        """This test checks the reverse of enumerate function"""
        self.assertEqual(list(rev_enumerate(["hey"])), list(enumerate(["hey"])))

    def test_find_second(self):
        """This test finds the second occurence of a character"""
        self.assertEqual((find_second("abc","abcaassadabcajk")),9)
        self.assertEqual((find_second("abc","ababcabcca")),5)
        self.assertEqual((find_second("iss","Mississippi")),4)
        self.assertEqual((find_second("abba","abbabba")),3)
        self.assertEqual((find_second("abba","zkdjfshn")),None)
        self.assertEqual((find_second("abba","abbacacs")),None)
     
    def test_get_lines(self):
        """This test yield the line without comment from the file""" 
        file_name = "C:/Users/Admin/Desktop/810/Readme.txt"
        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines(file_name))
        self.assertEqual(result, expect)


if __name__ == "__main__":
    unittest.main(exit = False,verbosity = 2)
