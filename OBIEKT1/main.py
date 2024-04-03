# def silnia(n):
#     iloczyn=1
#     for i in range(n):
#         iloczyn=iloczyn*(i+1)
#         print('element',i+1,'iloczyn',iloczyn)
#
#     ostatnia_cyfra=iloczyn%10
#     ostatnia_cyfra=str(iloczyn)
#     ostatnia_cyfra=ostatnia_cyfra[-1]
#     ostatnia_cyfra=int(ostatnia_cyfra)
#     return ostatnia_cyfra
#
# print(silnia(4))
#
# def silnia(n):
#     iloczyn=1
#     for i in range(n):
#         iloczyn=iloczyn*(i+1)
#         print('element',i+1,'iloczyn',iloczyn)
#
#     iloczyn=str(iloczyn)
#
#     i=1
#     while True:
#         if iloczyn.endswith('0'*i):
#             print('warunek spelniony dla ','0'*i)
#             i=i+1
#         else:
#             print('LICZBA ZER TO',i-1)
#             break
#     return iloczyn
#
# print(silnia(20))



# def zadanie3(str1,str2):
#     for i in range(1,len(str1)+1):
#         wzorzec=str1[0:i]
#         # print('idx',i,'prefix',wzorzec)
#         if str2.startswith(wzorzec):
#             pass
#             # print('zgadza sie ')
#         else:
#             if len(wzorzec[:-1])==0:
#                 return False
#             else:
#                 return wzorzec[:-1]
#
#
# print('zadanie3')
# prefix=zadanie3('abcd','abcbg')
# print(prefix)

# def zadanie4(lista):
#     licznik=0
#     for o in lista:
#         print(o)
#         if o[0] == o[-1]:
#             licznik=licznik+1
#     return licznik
# wynik=zadanie4(["ala","bc","kot","lol","uou"])
# print(wynik)

# def zadanie2(lista1,lista2):
#     licznik=0
#     for i in lista1:
#         print(i)
#         if i[0]==lista2(i[0]):
#             print(" ")
#     for i in lista2:
#         print(i)
#     return
# wynik=zadanie2(["Biały","Czarny","Czerwony"],["Czerwony","Zielony"])
# print(wynik)


# class najprostsza_klasa:
#     pass
#
# moj_pierwszy_obiekt=najprostsza_klasa()
# print(moj_pierwszy_obiekt)


# stack=[]
#
# def push(val):
#     stack.append(val)

# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# push(3)
# push(2)
# push(1)
#
# print(stack[1])
# print(pop())
# print(pop())
# print(pop())

# class Stack:
#     def _init_(self):
#         print("Cześć!")
#
# stackObject=Stack()

# class Stack:
#     def __init__(self):
#         self.__stackList = []
#     def push(self, val):
#         self.__stackList.append(val)
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
# stackObject = Stack()
# stackObject.push(3)
# stackObject.push(2)
# stackObject.push(1)
# print(stackObject.pop())
# print(stackObject.pop())
# print(stackObject.pop())

# ksiazki=[]
# class osoba:
#     pass
#
# y=int(input())
# ksiazki.append(y)
# def umiem():
#     if y<=5:
#         print( "NIE UMIESZ!")
#     else:
#         print( "UMIESZ!")
# umiem()

#
# class Trening:
#     pass
# a=int(input())
# def kroki():
#     while a!="zerój":
#         if a>0:
#             print("brakuje ci: ",1000-a,"kroków")
#             break
#         else:
#             print(0)
#             break
# wynik=kroki()
# print(wynik)



# class osoba:
#     def __init__(self):
#         self.__stackList = []
#     def przeczytane(self, ksiazka):
#         self.__stackList.append(ksiazka)
#     def umiem(self):
#         if len(self.__stackList)>=5:
#             print("umiem")
#         else:
#             print("Nie jestem gotowy przeczytałem ", len(self.__stackList))
#
# Janek=osoba()
# ksiazka=input("Ile przeczytałeś ksiązek:")
# Janek.przeczytane(ksiazka)
# Janek.umiem()
# ksiazka=input("Ile przeczytałeś ksiązek:")
# Janek.przeczytane(ksiazka)
# Janek.umiem()
# ksiazka=input("Ile przeczytałeś ksiązek:")
# Janek.przeczytane(ksiazka)
# Janek.umiem()
# ksiazka=input("Ile przeczytałeś ksiązek:")
# Janek.przeczytane(ksiazka)
# Janek.umiem()
# ksiazka=input("Ile przeczytałeś ksiązek:")
# Janek.przeczytane(ksiazka)
# Janek.umiem()

# class KlasaPrzykladowa:
#     def __init__(self, wartość = 1):
#         self.__pierwsza = wartość
#     def ustawDruga(self, wartość = 2):
#         self.__druga = wartość
#
# przykladowyObiekt1 = KlasaPrzykladowa()
# przykladowyObiekt2 = KlasaPrzykladowa(2)
# przykladowyObiekt2.ustawDruga(3)
# przykladowyObiekt3 = KlasaPrzykladowa(4)
# przykladowyObiekt3.__trzecia = 5
# print(przykladowyObiekt1.__dict__)
# print(przykladowyObiekt2.__dict__)
# print(przykladowyObiekt3.__dict__)
#

# class Samochod():
#     def __init__(self):
#         self.marka=input()
#         self.model=input()
#         self.rok_produkcji=input()
#         self.kolor=input()
#         self.predkosc()
#         self.spalanie()
#     def maks_predk(self):
#         self.(50)
#     def srednie_spalanie(self):
#         self.spalanie(5)
#     def info(self):
#         print(self.marka,self.model,self.rok_produkcji,self.kolor,self.predkosc,self.spalanie())
# Audi=Samochod()
# Mercedes=Samochod()
# Fiat=Samochod()
#     def

# class Osoba():
#     def __init__(self,imie):
#         self.imie=imie
#         self.ileKrokow=

# class Klasa():
#     def __init__(self):
#         self.imiona=[]
#
#     def ustawNazwe(self):
#         nazwa=input("Podaj nazwe klasy")
#         self.nazwa=nazwa
#
#     def dodajOsobe(self):
#         imie=input("Podaj imie osoby: ")
#         self.imiona.append(imie)
#     def sklad(self):
#         print(self.nazwa)
#         for i in self.imiona:
#             print(i)
# klasa1=Klasa()
# klasa1.ustawNazwe()
# for i in range(3):
#     klasa1.dodajOsobe()
# klasa1.sklad()

def zamiana(liczba):
z=0
y=1
        print("Twoja liczba:",liczba)
        print("Twój system:", x)
    if x==2




liczba=(input("Podaj liczbę: "))
x=int(input("Podaj System: "))
zamiana(liczba)

