import statistics
import csv
from pprint import pprint
#import pandas as pd

# Statistics is for dealing with the data, CVS is for reading the CVS format and Pandas is for converting CVS standard into a list

#imports NOT tested yet

print('Please type path for CVS')

x = input()

with open(x, newline='') as file:
    reader = csv.reader(file)
    res = list(map(tuple, reader))

pprint(res)






