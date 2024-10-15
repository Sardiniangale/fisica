
L = [int(x) for x in input("Enter the numbers in wanted in the average with commas\n").split(', ')]
print("\nThe values of input are", L) 


print('No errors detected proccessing list')

import statistics

x = statistics.mean(L)

print ('Your average is: ')
print (x)