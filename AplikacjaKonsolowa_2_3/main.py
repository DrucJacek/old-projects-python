
# Zadanie 2 -----------------------------------------
class Osoba:
    liczba_instancji = 0

    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.liczba_instancji += 1

    def kopiowanie(self, o):
        return Osoba(o.__id, o.__imie)

    def przywitanie(self,i):
        print("Cześć", i, "mam na imię", self.__imie)


print(Osoba.liczba_instancji)
osoba1 = Osoba(1, "Jan")
osoba2 = osoba1.kopiowanie(osoba1)
print(osoba1, osoba1.__dict__)
print(osoba2, osoba2.__dict__)
osoba1.przywitanie("Janusz")
print(Osoba.liczba_instancji)


# Zadanie 3 -----------------------------------------
class Notatka:
    __licznik = 0

    def __init__(self, tytul, tresc):
        Notatka.__licznik += 1
        self.__id = Notatka.__licznik
        self._tytul = tytul
        self._tresc = tresc

    def wyswietl(self):
        print(f"Tytuł: {self._tytul}\nTreść: {self._tresc}")

    def diagnostyka(self):
        print(f'Wszystkie dane: {self.__id}; {Notatka.__licznik}; {self._tytul}; {self._tresc} \n')


obj1 = Notatka("kot", "mój ulubiony kot to filo")
obj2 = Notatka("pies", "mój ulubiony pies to ariks")
obj3 = Notatka("koń", "konie są szybkie")
obj1.wyswietl()
obj1.diagnostyka()
obj2.wyswietl()
obj2.diagnostyka()
obj3.wyswietl()
obj3.diagnostyka()