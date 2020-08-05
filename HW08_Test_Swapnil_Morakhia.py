import unittest
from HW08_Swapnil_Morakhia import file_reading_gen

class TestModuleGeneratorFile(unittest.TestCase):

    def test_anagram_lst(self):
        """This checks the anagramas_list"""
        path = "C:/Users/Admin/Desktop/810/Readme.txt"

        self.assertTrue(file_reading_gen(path, 3, sep=',', header = False)) == (('CWID', 'Name', 'Majo2r'))

if __name__ == "__main__":
    unittest.main(exit = False,verbosity = 2)
