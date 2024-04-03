
x=int('011',2)
y=int('010',4)
z=int('010',8)
w=int('A3',16)

def zamianaz10doBazy(input_,baza):
    znaki=list()
    calkowita=int(input_)
    while calkowita>0:
        reszta=calkowita%baza
        calkowita =calkowita//baza
        znaki.append(reszta)
    znaki.reverse()

    if baza==16:
        for i in range(len(znaki)):

            if znaki[i]==10:
                znaki[i]='A'
            elif znaki[i]==11:
                znaki[i]='B'
            elif znaki[i] == 12:
                znaki[i] = 'C'
            elif znaki[i] == 13:
                znaki[i] = 'D'
            elif znaki[i] == 14:
                znaki[i] = 'E'
            elif znaki[i] == 15:
                znaki[i] = 'F'

    znaki_jako_str=[str(z) for z in znaki]
    return (''.join(znaki_jako_str))

def zamiana_miedzy_systemami(wartosc,baza_wejsciowa,baza_wyjsciowa):
    liczba_w_systemie_dziesietnym=int(wartosc,baza_wejsciowa)
    liczba_w_systemie_wyjsciowym=zamianaz10doBazy(liczba_w_systemie_dziesietnym,baza_wyjsciowa)
    return(liczba_w_systemie_wyjsciowym)

wartosc=input('Podaj liczbę: ')
baza_wejsciowa=int(input('Podaj system twojej liczby: '))
baza_wyjsciowa=int(input('Podaj system na jaki chcesz zamienić: '))
print(zamiana_miedzy_systemami(wartosc,baza_wejsciowa,baza_wyjsciowa))

Koniec=True