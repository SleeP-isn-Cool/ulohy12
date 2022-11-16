import tkinter

canvas=tkinter.Canvas(width=500,height=500,bg="white")

canvas.pack()

def pismo():
    canvas.delete("all")
    
    global pismo

    str = entry1.get()
    
    x = 0

    for char in str:
        canvas.create_text(x+250,250, text=char, fill="black")
        sleep(.50)
        x=x+15

    canvas.update()

entry1 = tkinter.Entry()
entry1.pack()
button1=tkinter.Button(text="píš",command=pismo)
button1.pack()

#neviem preco ale chladenie na macu ide na 30000% normalne sa bojim ze zhorim
