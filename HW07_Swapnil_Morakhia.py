from collections import defaultdict
from collections import Counter

def anagram_lst(str1,str2):
    """This returns True if 2 strings are anagrams"""
    return sorted(list(str1.lower())) == sorted(list(str2.lower()))

def anagrams_dd(str1, str2):
    """This returns true if 2 stings are angarams by default dictionary"""
    dd = defaultdict(int)

    for char in str1:
        dd[char] += 1

    for c in str2:
        if c in dd:
            dd[c] -= 1
        else:
            return False
                
    for each in dd:
        if dd.get(each) != 0: 
            return False
    
    for each in dd:
        if dd.get(each) == 0:
            return True

def anagrams_cntr(str1, str2):
    """This returns true if 2 strings are anagrams by Counter methods"""
    return Counter(str1) == Counter(str2)

def covers_alphabet(sentence):
    """This returns true if all the alphabates are covers atleast once in sentence"""
    dict1 = defaultdict(int)    
    my_alph = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    
    for char in my_alph:
        if char not in sentence:
            return False
        
    for char in my_alph:
        if char in sentence:
            return True
"""
def book_index(words):
    #This returns the list of words present in pages  
    list = []
    for tuple in words:
        for inner_list in list:
            if tuple[0] == inner_list[0]:

                if tuple[1] not in inner_list[1]:
                    for item in inner_list[1]:
                        if item >= tuple[1]:
                            inner_list[1].insert(inner_list[1].index(item), tuple[1])
                            break
                    else:
                        inner_list[1].append(tuple[1])
                break
        else:
            list.append([tuple[0],[tuple[1]]])
    return sorted(list)
"""


words = [('how',1), ('when',1), ('how',2), ('why',1), ('why',3), ('how',4),('when',2)]

def book_index(words):
    indx = 
    for word, page in words:
        indx[word].add(page)

    print([[word, sorted(list(indx[word]))] for word in sorted(indx.keys)])

book_index(words)