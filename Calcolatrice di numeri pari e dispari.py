import numpy as np

l=[] #lista vuota, punto di partenza

print('CALCOLATORE DI NUMERI PARI E DISPARI FINO AL NUMERO DESIDERATO')

n=int(input('Numero limite: ')) #metti fino a che numero vuoi controllare

for i in range(n//2+1): #n divisione intera per 2 per inserire nella lista i numeri pari solo fino al desiderato
    l.append(i*2)

for i in range(n+1):   #i due for vanno separati, non so perché ma funziona solo così
    if i in l:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

#if e else vanno alla stessa altezza, metto i due punti e il comando sotto