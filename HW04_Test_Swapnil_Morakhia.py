from HW_04_Swapnil_Morakhia import count_vowels, last_occurrencee, my_enumerate, Fraction
import unittest 

#Test Fraction class to test simplify method
class TestFraction(unittest.TestCase):
    def test_simplify(self):
        self.assertEqual(str(Fraction(5,20).simplify()),'1.0/4.0')
        self.assertEqual(str(Fraction(25,10).simplify()),'5.0/2.0')
        self.assertEqual(str(Fraction(5,13).simplify()),'5.0/13.0')
        

#Test Iteration to test other methods
class TestIteration(unittest.TestCase):

    #This checks if the count_vowels is working
    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)

    #This checks if the last occurrence is working  
    def test_last_occurrencee(self):
        self.assertEqual(last_occurrencee("python","o"), 4)
        self.assertEqual(last_occurrencee("python","p"), 0)
        self.assertEqual(last_occurrencee("hello world","p"), None)
    
    #This checks if the enumerate is workking
    def test_enumerate(self):
        self.assertEqual(list(my_enumerate("hey")), list(enumerate("hey")))
        self.assertEqual(list(my_enumerate(["h","e","y"])), list(enumerate(["h","e","y"])))


if __name__ == "__main__":
    unittest.main(exit = False,verbosity = 2)
    