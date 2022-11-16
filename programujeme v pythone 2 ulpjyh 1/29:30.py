from random import *

s = input("Zadaj reťazec: ")

novy = ''

for i in range(len(s)):
    ktory = randrange(len(s))
    print('Odstraňujem znak', s[ktory])
    novy = novy+s[ktory]
    print('Zatiaľ som vytvoril:', novy)
    s = s[:ktory]+s[ktory+1:]
    print('Ešte zostali tieto znaky:', s)
print('Zamiešané slovo:', novy)



#dakedy si myslim ze som genius kazdopadne dakujem za pozornost
