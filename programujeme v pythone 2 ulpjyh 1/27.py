''
vstup = input('Zadaj text:')
sifra = ""
for znak in vstup:
    novyznak = znak
    if "a" <= znak <= "z":
        novyznak = chr(ord(znak)-3)
    if znak == "a":
        novyznak = "x"
    if znak == "b":
        novyznak = "y"
    if znak == "c":
        novyznak = "z"
    sifra = sifra+novyznak
print(sifra)
''

#^ na 3
#v na 2


vstup = input('Zadaj text:')
sifra = ""
for znak in vstup:
    novyznak = znak
    if "a" <= znak <= "z":
        novyznak = chr(ord(znak)-2)
    if znak == "a":
        novyznak = "y"
    if znak == "b":
        novyznak = "z"
    sifra = sifra+novyznak
print(sifra)
