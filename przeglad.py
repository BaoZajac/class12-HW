import sys
from accountant import dotychczasowa_historia_operacji
from accountant import historia_na_dzialania
from accountant import historia_operacji
from accountant import manager


@manager.assign("przeglad")
def przeglad_func(abc):
    dotychczasowa_historia_operacji()

    historia_na_dzialania()

    for element in historia_operacji[int(sys.argv[2]):int(sys.argv[3])+1]:
        for element2 in element:
            print(element2)

    if historia_operacji[-1] != "stop":
        print("stop")


manager.execute("przeglad")
