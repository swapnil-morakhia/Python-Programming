class Fraction:
    
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def plus(self,other):
        new_num = (self.num * other.den) + (other.num * self.den)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def minus(self,other):
        new_num = (self.num * other.den) - (other.num * self.den)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def division(self,other):
        new_num= self.num * other.den
        new_den= self.den * other.num
        return Fraction(new_num, new_den)  
     
    def multiply(self,other):
        new_num = self.num * other.num  
        new_den = self.den * other.den
        return Fraction(new_num,new_den)

    def is_equal(self,other):
        if (self.num * other.den) == (self.den * other.num):
            print("both fractions are equal")
        else:
            print("both are unequal")
    
def main():
    while True:
        try:
            num1 = int(input(" Enter the num1: "))
            break
        except:
            print("Invalid input!")
    while True:
        try:
            den1 = int(input(" Enter the den1: "))
            if den1 == 0:
                raise ZeroDivisionError
            break
        except:
            print("Invalid input!")
    while True:
        try:
            num2 = int(input(" Enter the num2: "))
            break
        except:
            print("Invalid input!")
    while True:
        try:
            den2 = int(input(" Enter the den2: "))
            if den2 == 0:
                raise ZeroDivisionError
            break
        except:
            print("Invalid input!")
           
        
    f1 = Fraction(num1,den1)
    f2 = Fraction(den1,den2)
                
    user = input("enter your choice: \n 1:add \n 2:sub \n 3:divide \n 4:multiply \n 5:compare \n ")
    if user == "1":
        print(f1.plus(f2))
        #break
    elif user == "2":
        print(f1.minus(f2))
        #break
    elif user == "3":
        print(f1.division(f2))
        #break
    elif user == "4":
        print(f1.multiply(f2))
        #break
    elif user == "5":
        print(f1.is_equal(f2))
        #break
    else:
        print("Invalid input, pls try again\n")

def test_suite():
    print("Test_Suite Running")
    f12 = Fraction(1,2)
    f44 = Fraction(4,4)
    f128 = Fraction(12,8)
    f32 = Fraction(3,2)

    print(f"{f12} + {f12} = {f12.plus(f12)} [4/4] ")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8] ")
    print(f"{f12} + {f44} = {f12.plus(f44)} [12/8] ")
    print(f"{f128}==f{32} is {f128.is_equal(f32)} [True]")

if __name__ == '__main__':
    test_suite()
    main()
        

