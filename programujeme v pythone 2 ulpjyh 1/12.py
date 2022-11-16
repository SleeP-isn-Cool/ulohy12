Veta = input("Zadaj vetu: ")
Slová = Veta.split()
Slová_dĺžka = [len(slovo) for slovo in Slová if slovo!="the"]
print(Slová_dĺžka)
