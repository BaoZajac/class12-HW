from accountant import dotychczasowa_historia_operacji
from accountant import historia_na_dzialania
from accountant import manager


manager.execute("dotychczasowa_historia_operacji")
# dotychczasowa_historia_operacji()

saldo = historia_na_dzialania()[0]

print(saldo)
