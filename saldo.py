import sys
from accountant import dotychczasowa_historia_operacji
from accountant import historia_operacji
from accountant import historia_na_dzialania
from accountant import zapis_do_pliku
from accountant import manager


@manager.assign("saldo")
def saldo_func(abc):
    dotychczasowa_historia_operacji()

    # wczytanie danych wejsciowych uruchamiających program i zapisanie ich w historii operacji
    zmiana_na_koncie = sys.argv[2]
    nazwa_operacji = sys.argv[3]
    obecna_lista = (sys.argv[0][0:len(sys.argv[0])-3], zmiana_na_koncie, nazwa_operacji)
    historia_operacji.append(obecna_lista)
    historia_operacji.append(("stop",))

    saldo = historia_na_dzialania()[0]

    if saldo >= 0:
        zapis_do_pliku()


manager.execute("saldo")
