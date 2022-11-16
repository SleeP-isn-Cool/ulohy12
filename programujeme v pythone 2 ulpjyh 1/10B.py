import tkinter

canvas = tkinter.Canvas(width=500, height=500, bg="black")

canvas.pack()

def slovo():
    
    pismo = entry1.get()

    x=0

    uh = 0

    uhol = 360/(len(pismo)-1)

    for i in range(len(pismo)):
        x=x+25
        canvas.create_text(x+200, 250, text=pismo[i], fill="white", font="Arial 20", angle=uh)
        uh = uh - uhol


        
entry1 = tkinter.Entry()
entry1.pack()

button1 = tkinter.Button(text="píš", command=slovo)
button1.pack()
