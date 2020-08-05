from fractions import Fraction
import unittest
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self,other):
        new_num = (self.num * other.den) + (other.num * self.den)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self,other):
        new_num = (self.num * other.den) - (other.num * self.den)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self,other):
        new_num= self.num * other.den
        new_den= self.den * other.num
        return Fraction(new_num, new_den)  
     
    def __mul__(self,other):
        new_num = self.num * other.num  
        new_den = self.den * other.den
        return Fraction(new_num,new_den)

    #This checks whether both the fractions are equal
    def __eq__(self,other):
        return (self.num * other.den) == (self.den * other.num)

    #This checks whether the fractions are not equal
    def __ne__(self,other):
        return (self.num * other.den) != (self.den * other.num)
    
    #This returns true if the 1st fraction is less than the 2nd Fraction
    def __lt__(self,other):
        return (self.num * other.den) < (self.den * other.num)
    
    #This returns true if the 1st fraction is less than or equal to the 2nd Fraction
    def __le__(self,other):
        return (self.num * other.den) <= (self.den * other.num)

    #This returns true if the 1st fraction is greater than the 2nd Fraction
    def __gt__(self,other):
        return (self.num * other.den) > (self.den * other.num)

    #This returns true if the 1st fraction is greater than or equal to the 2nd Fraction
    def __ge__(self,other):
        return (self.num * other.den) >= (self.den * other.num)

def main():
    while True:
        try:
            num1 = float(input(" Enter the num1: "))
            break
        except:
            print("Invalid input!")
    while True:
        try:
            den1 = float(input(" Enter the den1: "))
            if den1 == 0:
                raise ZeroDivisionError
            break
        except:
            print("Invalid input!")
    while True:
        try:
            num2 = float(input(" Enter the num2: "))
            break
        except:
            print("Invalid input!")
    while True:
        try:
            den2 = float(input(" Enter the den2: "))
            if den2 == 0:
                raise ZeroDivisionError
            break
        except:
            print("Invalid input!")
           
    f1 = Fraction(num1,den1)
    f2 = Fraction(num2,den2)
     
    user = input("enter your choice: \n 1:add \n 2:sub \n 3:divide \n 4:__mul__ \n 5:compare \n ")
    if user == "1":
        print(f1.__add__(f2))
        #break
    elif user == "2":
        print(f1.__sub__(f2))
        #break
    elif user == "3":
        print(f1.__truediv__(f2))
        #break
    elif user == "4":
        print(f1.__mul__(f2))
        #break
    elif user == "5":
        print(f1.__eq__(f2))
        #break
    else:
        print("Invalid input, pls try again\n")

def test_suite():
    print("Test_Suite Running")
    f12 = Fraction(1,2)
    f44 = Fraction(4,4)
    f128 = Fraction(12,8)
    f32 = Fraction(3,2)

    print(f"{f12} + {f12} = {f12.__add__(f12)} [4/4] ")
    print(f"{f44} - {f12} = {f44.__sub__(f12)} [4/8] ")
    print(f"{f12} + {f44} = {f12.__add__(f44)} [12/8] ")
    print(f"{f128}==f{32} is {f128.__eq__(f32)} [True]")

#unittest
class TestFraction(unittest.TestCase):
    #Testing the Fraction      
    def test_init(self):        
        f = Fraction(3, 4)        
        self.assertEqual(f.num, 3)        
        self.assertEqual(f.den, 4)  

    #Testing the fraction output
    def test_str(self):
        f = Fraction(3, 4)        
        self.assertEqual(str(f), '3/4')
    
    #This test adds the 2 fractions and returns the result
    def test_add(self):
        f1 = Fraction(3, 4)        #3/4 = 0.75
        f2 = Fraction(1, 2)        #1/2 = 0.5
        f3 = Fraction(1, 3)        #1/3 = 0.33
        self.assertTrue((f1 + f1) == Fraction(6, 4))        
        self.assertTrue((f1 + f2) == Fraction(5, 4))        
        self.assertTrue((f1 + f3) == Fraction(13, 12))
        self.assertFalse((f1 + f2) == Fraction(4, 5))

    #This test subtracts the 2 fractions and returns the result
    def test_subtraction(self):
        f1 = Fraction(3, 4)        #3/4 = 0.75
        f2 = Fraction(1, 2)        #1/2 = 0.5
        f3 = Fraction(1, 3)        #1/3 = 0.33
        self.assertTrue((f1 - f1) == Fraction(0, 0))        
        self.assertTrue((f1 - f2) == Fraction(1, 4))        
        self.assertTrue((f1 - f3) == Fraction(5, 12))
        self.assertFalse((f1 - f2) == Fraction(4, 5))
    
    #This test divides the 2 fractions and returns the result  
    def test_divison(self):
        f1 = Fraction(3, 4)        #3/4 = 0.75
        f2 = Fraction(1, 2)        #1/2 = 0.5
        f3 = Fraction(1, 3)        #1/3 = 0.33
        self.assertFalse((f1 / f1) == Fraction(6, 4))        
        self.assertTrue((f1 / f2) == Fraction(3, 2))        
        self.assertTrue((f1 / f3) == Fraction(9, 4))

    #This test multiplies the 2 fractions and returns the result 
    def test_multiplication(self):
        f1 = Fraction(3, 4)        #3/4 = 0.75
        f2 = Fraction(1, 2)        #1/2 = 0.5
        f3 = Fraction(1, 3)        #1/3 = 0.33
        self.assertFalse((f1 * f1) != Fraction(9, 16))        
        self.assertTrue((f1 * f2) == Fraction(3, 8))        
        self.assertTrue((f1 * f3) == Fraction(3, 12))
        self.assertFalse((f1 * f2) == Fraction(1, 4))

    #This test checks whether the 2 equations are equal
    def test_equal(self):
        f1 = Fraction(3, 4)        
        f2 = Fraction(1, 2)       
        f3 = Fraction(2, 4)
        self.assertFalse (f1 == f2)
        self.assertTrue (f2 == f3)
        self.assertFalse(f1 == Fraction(3, 5))

    #This test checks whether the 2 fractions are not equal
    def test_not_equal(self):
        f1 = Fraction(3, 4)        
        f2 = Fraction(1, 2)       
        f3 = Fraction(2, 4)
        self.assertFalse (f3 != f2)
        self.assertTrue (f1 != f3)

    #This test checks which fraction is less 
    def test_less_than(self):
        f1 = Fraction(3, 4)        #3/4 = 0.75
        f2 = Fraction(1, 2)        #1/2 = 0.5
        f3 = Fraction(1, 3)        #1/3 = 0.33
        self.assertTrue(f2 < f1)
        self.assertFalse(f1 < f3)
        self.assertTrue(f2 <(Fraction(3,4)))
    
    #This test checks if fraction is less than or equal to
    def test_less_than_equal(self):
        self.assertTrue((Fraction(1,3))<=(Fraction(2,6))) 
        self.assertTrue((Fraction(1,3))<=(Fraction(7,6)))
    
    #This test checks which fraction is greater
    def test_greater_than(self):
        f1 = Fraction(3, 4)        #3/4 = 0.75
        f2 = Fraction(1, 2)        #1/2 = 0.5
        f3 = Fraction(1, 3)        #1/3 = 0.33
        self.assertTrue(f1 > f2)
        self.assertFalse(f3 > f1)
        self.assertTrue((Fraction(3,4))> f2)

    #This test checks if fraction is greater than or equal to
    def test_greater_less_than_equal(self):
        self.assertTrue((Fraction(2,6))>=(Fraction(1,3))) 
        self.assertTrue((Fraction(7,6))>=(Fraction(1,3)))
    
if __name__ == '__main__':
    #test_suite()
    unittest.main(exit=False, verbosity=2)
    #main()