def reverse(string):
    """This returns the reverse of a string"""
    rev = ""
    n = len(string)
    while n > 0:
        rev = rev + string[n - 1]
        n = n - 1
    return rev

def rev_enumerate(sequence):
    """This returns the reverse of enumerate function"""
    num = len(sequence) 
    for c in sequence:
        num = num - 1
        yield (num, sequence[num])

def find_second(target, string):
    """This function finds the second ocurrence of target in string"""
    available = string.find(target)
    new_available = 0
    new_string = ""
    if available >= 0:  #for 1st occurrence
        new_string = new_string + string[available + 1: ]
        new_available = new_string.find(target)
        if new_available > 0: #for 2nd occurence
            new_available = new_available + available + 1
            return new_available

print(find_second("hello","l"))

def get_lines(path):
    """This function yield the line without comment from the file"""
    with open(path) as fp:
        for line in fp:
            line = line.rstrip("\n")        
            while line.endswith("\\"):  
                line = line[:-1] + fp.readline().rstrip("\n")

            if not line.startswith("#"):
                line = line.split("#",1)[0]
                line = line.strip()
                yield line