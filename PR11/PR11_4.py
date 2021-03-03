from tkinter import *

root = Tk()
root.resizable(False,False)
c = Canvas(root, width=200, height=185, bg='white')
c.pack()

c.create_rectangle(60, 80, 140, 160,
                   fill='light blue',
                   outline='light blue')
c.create_polygon((40, 80), (160, 80), (100, 30),
                 fill='light blue',
                 outline='light blue')
c.create_oval(160, 10, 195, 45,
              fill='orange',
              outline='yellow')
x1 = -5
x2 = 15
for i in range(25):
        c.create_arc(x1, 155, x2, 265,
                     start=160, extent=-70,
                     style=ARC, outline='dark green',
                     width=2)
        x1+=10
        x2+=10

root.mainloop()
