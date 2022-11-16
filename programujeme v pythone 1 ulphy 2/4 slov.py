import tkinter

from random import *

canvas = tkinter.Canvas(width=400, height=400)

canvas.pack()

#nefunguje strasna sprostost

x=200
y=0
    
def kresli_kurzor(x, y):
    canvas.create_line(x, y, x+50, y, fill='blue', width=5)
    
def vypis_body(pocet_bodov):
    canvas.create_text(100, 10, text='Počet získaných bodov:')
    canvas.create_text(200, 10, text=pocet_bodov)
    
def timer1(x,y):
    zle = choice(("vyndows","mack","cybuľa","fizyka","kupym","mynulu","cygan","dobri den","kupyt"))
    dobre = choice(("Mac", "Cesnak", "Hora", "Koza", "Euro","Nemám", "Nápady", "Mám", "Rád", "Beladický","Mekáč", "Samozrejme", ""))
    text = choice((zle, dobre))
    canvas.delete('all')

    canvas.create_text(x, y,text=text, fill="white")
    
    global lopticka_x, lopticka_y, pocet_bodov
    
    lopticka_y = lopticka_y + 15
    kresli_lopticku(lopticka_x, lopticka_y) 

    kresli_kurzor(kurzor_x, kurzor_y)
    vypis_body(pocet_bodov)
    
    if kurzor_x<lopticka_x<kurzor_x+50 and kurzor_y-10<lopticka_y<kurzor_y and text==dobre:
        pocet_bodov = pocet_bodov + 1
        lopticka_x = randrange(300)
        lopticka_y = 20

    if kurzor_x<lopticka_x<kurzor_x+50 and kurzor_y-10<lopticka_y<kurzor_y and text==zle:
        pocet_bodov = pocet_bodov - 1
        lopticka_x = randrange(300)
        lopticka_y = 20
        
    if lopticka_y>300 and text==dobre:
        pocet_bodov = pocet_bodov - 1
        lopticka_x = randrange(300)
        lopticka_y = 10

    if lopticka_y>300 and text==zle:
        pocet_bodov = pocet_bodov + 1
        lopticka_x = randrange(300)
        lopticka_y = 10
        
    canvas.after(20, timer1)
    
def posun_mysi(suradnice):
    global pocet_bodov, kurzor_x
    
    kurzor_x = suradnice.x
    
    canvas.delete('all')
    
    kresli_lopticku(lopticka_x, lopticka_y)
    kresli_kurzor(kurzor_x, kurzor_y)
    vypis_body(pocet_bodov)


pocet_bodov = 0
lopticka_x = randrange(300)
lopticka_y = 20
kurzor_x = 150
kurzor_y = 250
timer1()    
canvas.bind('<Motion>', posun_mysi)
