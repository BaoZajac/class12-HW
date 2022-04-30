import sys
from accountant import dotychczasowa_historia_operacji
from accountant import historia_operacji
from accountant import historia_na_dzialania
from accountant import zapis_do_pliku
from accountant import manager


@manager.assign("sprzedaz")
def sprzedaz_func(abc):
    dotychczasowa_historia_operacji()

    # wczytanie danych wejsciowych uruchamiających program i zapisanie ich w historii operacji
    nazwa_zakup = sys.argv[2]
    cena_jednostkowa = sys.argv[3]
    liczba_sztuk = sys.argv[4]
    obecna_lista = (sys.argv[0][0:len(sys.argv[0])-3], nazwa_zakup, cena_jednostkowa, liczba_sztuk)
    historia_operacji.append(obecna_lista)
    historia_operacji.append(("stop",))

    if historia_na_dzialania() == "Błąd":
        print("Błąd")
    else:
        zapis_do_pliku()


manager.execute("sprzedaz")
