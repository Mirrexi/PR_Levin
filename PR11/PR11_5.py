from tkinter import *


def test(event):
    vivod.configure(text=f'X:{event.x}, Y:{event.y}')


window = Tk()
window.title('Интерфейс')
window.geometry('640x640')
window.bind('<Button-1>', test)
vivod = Label(window, text='', font=('Comic Sans ms', 10))
vivod.grid(column=0, row=0)

window.mainloop()
