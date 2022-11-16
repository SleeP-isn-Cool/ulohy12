import tkinter

canvas = tkinter.Canvas(width=500, height=500)

canvas.pack()

canvas.create_rectangle(0,420,500,500, fill="blue", outline="blue")

def cigan(suradnice):
    x = suradnice.x
    y = suradnice.y
#lod
    if y > 420:
        canvas.create_line(x-20,y, x+20,y, width=2)
        canvas.create_line(x-15,y+10, x+15,y+10, width=2)
        canvas.create_line(x-20, y, x-15, y+10, width=2)
        canvas.create_line(x+20, y, x+15, y+10, width=2)
        canvas.create_line(x,y,x,y-20, width=2)
        canvas.create_line(x,y-20,x+5,y-15,x,y-10)
#balon
    if y < 420:
        canvas.create_rectangle(x-5,y-5, x+5, y+5, fill="white")

        canvas.create_oval(x-10, y-30, x+10, y-10, fill="blue")

        canvas.create_line(x, y-5, x-10,y-20, fill="black" )

        canvas.create_line(x, y-5, x+10,y-20, fill="black" )
            
        
canvas.bind('<Button-1>', cigan)
