"""
Author name: Swapnil Morakhia
Purpose: Assignemnt 4
Date: 25th September 2019
"""

from fractions import Fraction
#this method counts the num of vowels in a string
def count_vowels(s):            
    s = s.lower()
    count = 0 
    vowels = ["a","e","i","o","u"]
    for alphabet in s:
        if alphabet in vowels:
            count += 1
    return count

 
#this method returns the last occurence character 
def last_occurrencee(sequence,target):
    last_occur = -1
    for i in range(len(sequence)):
        if(sequence[i] == target):
            last_occur = i
        
    if last_occur == -1:
        return None
    else:
        return last_occur


#this method creates my own enumerate method
def my_enumerate(seq):
    for num in range(len(seq)): 
        yield (num , seq[num])


#This is a fraction class 
class Fraction:

    #initialize the fractions
    def __init__(self, num, den):
        self.num = num
        self.den = den

    #this is __str__ magic method
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    #this simplifies the fraction (Reduces the fractions)
    def simplify(self):
        #if numerator == denominator
        if self.num == self.den:
            new_num = 1
            new_den = 1
            return Fraction(new_num, new_den)
        #if numerator is smaller
        elif self.num < self.den:
            for i in range((self.den)-1,0,-1):
                if self.num % i == 0 and self.den % i == 0:
                    new_num = self.num / i
                    new_den = self.den / i
                    return Fraction(new_num, new_den)
        #if denominator is smaller
        else:
            for i in range ((self.num)-1,0,-1):
                if self.num % i == 0 and self.den % i == 0:
                    new_num = self.num / i
                    new_den = self.den / i
                    return Fraction(new_num,new_den)   
