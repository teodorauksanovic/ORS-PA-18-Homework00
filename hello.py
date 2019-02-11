korisnikunioprvi = input("unesiteprvibroj:")
korisnikuniodrugi = input("unesitedrugibroj:")


if (not korisnikunioprvi.isnumeric()) or (not korisnikuniodrugi.isnumeric()):
    print("niste unijeli broj")
    quit()


brojprvi = int(korisnikunioprvi)
brojdrugi = int(korisnikuniodrugi)



zbir = brojprvi + brojdrugi
print(zbir)

