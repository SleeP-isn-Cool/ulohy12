import random

pismena = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ"

for i in range(0, 1):
    

    heslo = ""

    for i in range(0, 8):
        heslopis = random.choice(pismena)
        heslo    = heslo + heslopis
    print("Tu máš svoje heslo: ", heslo)
