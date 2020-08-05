def list_copy(l):
    """This method returns the copy of the list"""
    return[word for word in l]

def list_intersect(l1,l2):
    """This method returns the common elements within the 2 lists"""
    return[word for word in l1 if word in l2]

def list_difference(l1, l2):
    """This method returns the uncommon elements within the 2 lists""" 
    return[word for word in l1 if word not in l2]

def remove_vowels(string):
    """This method removes the vowels in the string"""
    return "".join([i for i in string if i.lower() not in "aeiou"]) 

def check_pwd(password):
    """This method checks the password criteria""" 
    return all([any(c.isupper() for c in password), any(c.islower() for c in password), password[-1].isdigit()])

def insertion_sort(l):
    """This method sorts the list with the help of insertion sort"""
    new_l = []
    if len(l) == 0:
        return new_l                   
    else:
        new_l.append(l[0])

    for x in range (1,len(l)):
        new_l.append(l[x])
        if  new_l[x] < new_l[x-1]:      
            for y in range(x,0,-1):
                if new_l[y] < new_l[y-1]:
                    new_l[y-1], new_l[y] = new_l[y], new_l[y-1] 
                else:
                    break
    return(new_l)
