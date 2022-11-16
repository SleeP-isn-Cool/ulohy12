import random

retazec = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

for i in range(0, 1):
    print(i)
    prazdne = ""   
    for i in range(0, 30):
        pis = random.choice(retazec)
        prazdne    = prazdne + pis
    print(prazdne)
