
# Zad 1 -----------------------------------------------
class Film:
    def __init__(self):
        self._tytul = ""
        self._liczba_wypozyczen = 0

    def get_liczba_wypozyczen(self):
        return self._liczba_wypozyczen

    def set_tytul(self, tytul):
        if len(tytul) > 20:
            print("Tytuł może mieć maksymalnie 20 znaków")
        else:
            self._tytul = tytul

    def get_tytul(self):
        return self._tytul

    def increment_liczba_wypozyczen(self):
        self._liczba_wypozyczen += 1


film = Film()
film.set_tytul("James Bond")

print("Tytuł filmu:", film.get_tytul())
print("Liczba wypożyczeń przed inkrementacją:", film.get_liczba_wypozyczen())
film.increment_liczba_wypozyczen()
print("Liczba wypożyczeń po pierwszej inkrementacji:", film.get_liczba_wypozyczen())
film.increment_liczba_wypozyczen()
print("Liczba wypożyczeń po drugiej inkrementacji:", film.get_liczba_wypozyczen())





