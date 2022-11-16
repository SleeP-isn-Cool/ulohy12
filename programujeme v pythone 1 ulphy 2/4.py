import tkinter
import random

canvas = tkinter.Canvas(width=500, height=500, bg="white")

canvas.pack()
entry1 = tkinter.Entry()
entry1.pack()

    #nefunguje vazne chujovina uz
for i in range(1,11):
    fsajkbcaskbf = str(entry1)
    x = random.randint(1, 500)
    y = random.randint(1, 500)
    
    #canvas.create_text(text=entry1 , x*i , y*i  )
    canvas.create_text(x*i, y*i, text=str(entry1), fill="black")

