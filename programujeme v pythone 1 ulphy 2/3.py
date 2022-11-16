import tkinter
from random import *

canvas = tkinter.Canvas(width=500, height=500)

canvas.pack()

sx = randint(0,7)

sy = randint(0,7)

def timer1():
    canvas.delete('all')
    velkost = 50
    sx = randint(0,7)
    sy = randint(0,7)
    canvas.create_text(200, 250, text=sx, font="Arial 30")
    canvas.create_text(300, 250, text=sy, font="Arial 30")
    canvas.create_text(100, 10, text='Počet získaných bodov:')
    canvas.create_text(200, 10, text=pocet_bodov)
    canvas.after(500, timer1)
        
def klik(suradnice):
    global pocet_bodov
    x = suradnice.x
    y = suradnice.y
    if sx == sy:
        pocet_bodov = pocet_bodov + 1
    if sx != sy:
        pocet_bodov = pocet_bodov - 1

pocet_bodov = 0

timer1()

canvas.bind("<Button-1>", klik)
