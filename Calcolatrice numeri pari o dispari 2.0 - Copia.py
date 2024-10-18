l=[]

print('CALCOLATORE DI NUMERI PARI E DISPARI FINO AL NUMERO DESIDERATO')

print('ATTENZIONE: in caso si risponda yes, evitare numeri numeri troppo alti')

answer=input('Scrivere yes (o si) se si desidera calcolare tutti i numeri, no se il numero d'"'interesse è solo l'"'ultimo: ')

n=int(input('Numero: ')) #metti fino a che numero vuoi controllare

print('CALCOLATORE DI NUMERI PARI E DISPARI FINO AL NUMERO DESIDERATO')

if answer.lower()=='yes' or 'si':

    for i in range(n//2+1): #n divisione intera per 2 per inserire nella lista i numeri pari solo fino al desiderato
        l.append(i*2)

    for i in range(n+1):   #i due for vanno separati, non so perché ma funziona solo così
        if i in l:
            print(f'{i} is even')
        else:
            print(f'{i} is odd')

elif answer.lower()=='conad': #easter egg per verificare quanti elif si possono mettere
    print('Conad is love, Conad is life')

elif answer.lower()=='no':
    print('Per gentil cortesia rispondi solo con yes o no')

    if n//2!=(n-1)//2:
        print(f'{n} is even')
    else:
        print(f'{n} is odd')

else: #in caso uno non risponda a modo
    print('Per gentil cortesia rispondi solo con yes o no')