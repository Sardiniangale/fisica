#condizioni iniziali
t='y' #valore iniziale di t diverso da no
l=[]  #insieme vuoto, punto di partenza per quando a == yes o si

#titoli
print('CALCOLATORE DI NUMERI PARI E DISPARI FINO AL NUMERO DESIDERATO')

print('ATTENZIONE: in caso si risponda yes, evitare numeri numeri troppo alti')

a=input('Scrivere yes (o si) se si desidera calcolare tutti i numeri, no se il numero d'"'interesse è solo l'"'ultimo: ') #i valori di a ed n vanno messi prima di while sennò le condizioni di while non hanno una base
n=int(input('Numero: '))  #metti fino a che numero vuoi controllare

#while type(n)!=int:           #correzione di n
    #n=input('Numero: ')


while t.lower()!='no': #finché uno non risponde di no queste righe sottostanti verranno ripetute


    while (a.lower() not in {'yes','si','no','conad','franco'}):   #fincé il valore di a non rientra in quell'insieme verranno ripetute queste lines

        print('Per gentil cortesia rispondi solo con yes o no')

        a=input('Scrivere yes (o si) se si desidera calcolare tutti i numeri, no se il numero d'"'interesse è solo l'"'ultimo: ')

        n=int(input('Numero: '))


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


    if n==69:             #altro easter egg con n
        print('Shrek')


    if (a.lower()=='franco' and n==126):   #ennesimo easter egg per testare and
        print('Franco126')


    t=input('If you would like to stop using the calculator type no, else press Enter: ') #possibilità di porre fine al loop eguagliando 't' a 'no'
    if t.lower()!='no':

        a=input('Scrivere yes (o si) se si desidera calcolare tutti i numeri, no se il numero d'"'interesse è solo l'"'ultimo: ')

        n=int(input('Numero: '))        #riassegnazione dei valori di a ed n



