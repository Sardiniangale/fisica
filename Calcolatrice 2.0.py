l=[]

r=['yes','si','no','conad']

print('CALCOLATORE DI NUMERI PARI E DISPARI FINO AL NUMERO DESIDERATO')

print('ATTENZIONE: in caso si risponda yes, evitare numeri numeri troppo alti')

a=input('Scrivere yes (o si) se si desidera calcolare tutti i numeri, no se il numero d'"'interesse è solo l'"'ultimo: ')

n=int(input('Numero: ')) #metti fino a che numero vuoi controllare

t='y' #valore iniziale di t diverso da no

while t.lower()!='no': #finché uno non risponde di no queste righe sottostanti verranno ripetute

    while (a.lower() in r is True):

        print('Per gentil cortesia rispondi solo con yes o no')

        a=input('Scrivere yes (o si) se si desidera calcolare tutti i numeri, no se il numero d'"'interesse è solo l'"'ultimo: ')

        n=int(input('Numero: ')) #metti fino a che numero vuoi controllare


    if (a.lower() == 'yes' or a.lower()=='si'):

        for i in range(n//2+1): #n divisione intera per 2 per inserire nella lista i numeri pari solo fino al desiderato
            l.append(i*2)

        for i in range(n+1):   #i due for vanno separati, non so perché ma funziona solo così
            if i in l:
                print(f'{i} is even')
            else:
                print(f'{i} is odd')


    elif a.lower()=='no':   #else if perché non è il complementare dell'if soprastante

        if n//2!=(n-1)//2:
            print(f'{n} is even')
        else:
            print(f'{n} is odd')


    elif a.lower()=='conad': #easter egg per verificare quanti elif si possono mettere
        print('Conad is love, Conad is life')


    elif n==69:              #easter egg per verificare quanti elif si possono mettere
        print('Shrek')


    t=input('If you would like to stop using the calculator type no, else type wathever you want: ') #possibilità di porre fine al loop eguagliando 't' a 'no'
    if t.lower()!='no':

        a=input('Scrivere yes (o si) se si desidera calcolare tutti i numeri, no se il numero d'"'interesse è solo l'"'ultimo: ')

        n=int(input('Numero: '))                        #riassegnazione dei valori di a ed n
