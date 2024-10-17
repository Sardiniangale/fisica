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

#prove su come funziona il for dato che non l'ho capito
for i in range(12):
    print(f'{i+2.} free lunches at Conad')
    print(f'{i*2} paid lunches at Conad') #i due print li fa alternati per il loop?

#per quanto riguarda quello scritto qua sotto non mi ricordo dove volessi arrivare ma di sicuro non ha funzionato
p='no thanks'
for p in range(3):
    print(p)



