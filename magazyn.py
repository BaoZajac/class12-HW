import sys
from accountant import dotychczasowa_historia_operacji
from accountant import historia_na_dzialania
from accountant import manager


@manager.assign("magazyn")
def magazyn_func(abc):
    dotychczasowa_historia_operacji()

    magazyn = historia_na_dzialania()[1]

    for idx in sys.argv[2:]:
        if magazyn.get(idx):
            print(idx, ":", magazyn[idx])
        else:
            print(idx, ": brak w magazynie")


manager.execute("magazyn")
