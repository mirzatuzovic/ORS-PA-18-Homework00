korisnik_unio_prvi = input("Unesite prvi broj: ")
korisnik_unio_drugi = input("Unesite drugi broj: ")

if (not korisnik_unio_prvi.isnumeric() or not korisnik_unio_drugi.isnumeric()):
    print("Nijeste unijeli dobar broj")
    quit()

broj_prvi = int(korisnik_unio_prvi)    #prebacanje stringa u integer
broj_drugi = int(korisnik_unio_drugi)

zbir = broj_prvi + broj_drugi
print(zbir)
