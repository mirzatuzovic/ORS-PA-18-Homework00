def validni_brojeve(x, y):
    if not x.isnumeric() or not y.isnumeric():
        return False
    else:
        return True

korisnik_unio_prvi = input("Unesite prvi broj: ")
korisnik_unio_drugi = input("Unesite drugi broj: ")

if not validni_brojeve(korisnik_unio_prvi, korisnik_unio_drugi):
    quit("Brojevi nisu valdni")

broj_prvi = int(korisnik_unio_prvi)
broj_drugi = int(korisnik_unio_drugi)

zbir = broj_prvi + broj_drugi
print(zbir)