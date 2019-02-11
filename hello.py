def validnibrojevi(x,y):
    if not x.isnumeric() or not y.isnumeric():
        return False
    else:
        return True


korisnikunioprvi = input("unesiteprvibroj:")
korisnikuniodrugi = input("unesitedrugibroj:")


if not validnibrojevi(korisnikunioprvi, korisnikuniodrugi):
    quit("brojevi nisu validni")

brojprvi = int(korisnikunioprvi)
brojdrugi = int(korisnikuniodrugi)



zbir = brojprvi + brojdrugi
print(zbir)