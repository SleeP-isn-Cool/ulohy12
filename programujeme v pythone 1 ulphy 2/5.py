import tkinter

canvas = tkinter.Canvas(width=505, height=300, bg="black")

canvas.pack()

#semafor

canvas.create_line(101,0,101,500, width=3, fill="white")

canvas.create_line(202,0,202,500, width=3, fill="white")

canvas.create_line(303,0,303,500, width=3, fill="white")

canvas.create_line(404,0,404,500, width=3, fill="white")

canvas.create_oval(3, 3, 99, 99, fill="red")

canvas.create_oval(3,101,99, 198, fill="yellow")

canvas.create_oval(104, 201, 200, 297, fill="lime")

canvas.create_oval(205, 201, 301, 297, fill="lime")

canvas.create_oval(205, 3, 301, 99, fill="red")

canvas.create_oval(205,101,301, 198, fill="yellow")

canvas.create_oval(306,101,402, 198, fill="yellow")

canvas.create_oval(407, 3, 503, 99, fill="red")

