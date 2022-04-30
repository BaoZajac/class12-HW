from accountant import dotychczasowa_historia_operacji
from accountant import historia_na_dzialania
from accountant import manager


@manager.assign("konto")
def konto_func(abc):
    dotychczasowa_historia_operacji()
    saldo = historia_na_dzialania()[0]
    print(saldo)


manager.execute("konto")
