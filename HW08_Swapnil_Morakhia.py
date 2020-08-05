import os
from datetime import datetime, timedelta

def date_arithmetic():

    date1 = "Feb 27, 2000"
    date2 = "Feb 27, 2017"
    date3 = "Jan 1, 2017" 
    date4 = "Oct 31, 2017"    
    d1 = datetime.strptime(date1, "%b %d, %Y")
    d2 = datetime.strptime(date2, "%b %d, %Y")
    d3 = datetime.strptime(date3, "%b %d, %Y")
    d4 = datetime.strptime(date4, "%b %d, %Y")
    num_days = 3
    
    three_days_after_02272000 = (d1 + timedelta(days = num_days)).strftime("%b %d, %Y")
    three_days_after_02272017 = (d2 + timedelta(days = num_days)).strftime("%b %d, %Y")
    days_passed_01012017_10312017 = (d4 - d3).days
    
    return (three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017)

def file_reading_gen(path, fields, sep=',', header = False):
    
    try:
        fp = open(path, "r")
    except FileNotFoundError:
        print("No file found")
    else:
        with fp:
            num = 0
            for line in fp:
                list_line = line.rstrip().split(sep)
                num += 1
                if header == False:
                    header = True
                    continue
                
                if len(list_line) != fields:
                    raise ValueError(f'{path} has {len(list_line)} fields on line {num} but expected {fields}')
                
                yield (tuple(list_line))
                
class FileAnalyzer:
    """ Your docstring should go here for the description of the class."""
    def __init__(self, directory):
        """ Your docstring should go here for the description of the method."""
        self.directory = directory # NOT mandatory!
        self.files_summary = dict() 

        self.analyze_files() # summerize the python files data

    def analyze_files(self):
        """ Your docstring should go here for the description of the method."""        
        pass
        
    def pretty_print(self):
        """ Your docstring should go here for the description of the method."""
        pass # implement your code here

"""
dir = 'C:\\Users\\Admin\\Desktop\\810'

l1 = os.listdir(dir)
l2 = list()
count_lines = 0
characters = 0
for files in l1:
    if files.endswith(".py"):
        l2.append(files)

for each in l2:
    file_name = each
    print(each)

    fpp = open(os.path.join(dir, file_name), "r")
    for line in fpp:
        count_lines+=1
    print(count_lines)        
    C:/Users/Admin/AppData/Local/Programs/Python/Python37-32/python.exe 
"""
