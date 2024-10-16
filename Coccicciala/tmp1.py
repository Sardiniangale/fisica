import statistics
l = [int(x) for x in input("Enter the values you want\n").split(',')]
print("the values inserted are: ")
print(l)

x = statistics.median(l)
print("your median is: ")
print(x)

y = statistics.mean(l)
print("your mean is: ")
print(y)


z = statistics.mode(l)
print("the mode is: ")
print(z)




