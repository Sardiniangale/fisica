
l=[] #lista vuota, punto di partenza

print('CALCOLATORE DI NUMERI PARI E DISPARI FINO AL NUMERO DESIDERATO')

answer=input('Scrivere yes se si desidera calcolare tutti i numeri, no se il numero d'"'interesse è solo l'"'ultimo: ')

n=int(input('Numero limite: ')) #metti fino a che numero vuoi controllare

if answer.lower()=='yes': #lower così se uno risponde in caps va bene uguale

    for i in range(n//2+1): #n divisione intera per 2 per inserire nella lista i numeri pari solo fino al desiderato
        l.append(i*2)

    for i in range(n+1):   #i due for vanno separati, non so perché ma funziona solo così
        if i in l:
            print(f'{i} is even')
        else:
            print(f'{i} is odd')

elif answer.lower()=='no':
    for i in range(n//2+1):
        l.append(i*2)

    if n in l:
        print(f'{n} is even')
    else:
        print(f'{n} is odd')

elif answer.lower()=='conad': #easter egg per verificare quanti elif si possono mettere
    print('Conad is love, Conad is life')

else: #in caso uno non risponda a modo
    print('Per gentil cortesia rispondi solo con yes o no')


#if e else vanno alla stessa altezza, metto i due punti e il comando sotto

#Non funziona bene per grandi numeri