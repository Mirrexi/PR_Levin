from tkinter import *
from tkinter import messagebox


def add_digit(digit):
    calc.insert(len(calc.get()), digit)


def AC():
    calc.delete(0, END)


def DEL():
    calc.delete(len(calc.get()) - 1, END)


def RAVNO():
    try:
        result = eval(calc.get())
        AC()
        add_digit(result)
    except Exception:
        messagebox.showinfo('ERROR', 'Неправильное выражение')


window = Tk()
window.title('Калькулятор')
window.geometry(f'308x387')
window.resizable(False, False)

calc = Entry(window, width=19, font=('Comic Sans MS', 20), justify=RIGHT)
calc.grid(column=0, row=0, columnspan=4, stick='we')

btn_AC = Button(window, text='AC', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
                command=lambda: AC())
btn_AC.grid(column=0, row=1, stick="wens")
btn_del = Button(window, text='del', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
                 command=lambda: DEL())
btn_del.grid(column=1, row=1, stick="wens")
btn_percent = Button(window, text='%', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
                     command=lambda: add_digit('%'))
btn_percent.grid(column=2, row=1, stick="wens")
btn_delit = Button(window, text='/', bg='orange', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
                   command=lambda: add_digit('/'))
btn_delit.grid(column=3, row=1, stick="wens")
btn_7 = Button(window, text='7', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
               command=lambda: add_digit(7))
btn_7.grid(column=0, row=2, stick="wens")
btn_8 = Button(window, text='8', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
               command=lambda: add_digit(8))
btn_8.grid(column=1, row=2, stick="wens")
btn_9 = Button(window, text='9', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
               command=lambda: add_digit(9))
btn_9.grid(column=2, row=2, stick="wens")
btn_umnoj = Button(window, text='x', bg='orange', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
                   command=lambda: add_digit('*'))
btn_umnoj.grid(column=3, row=2, stick="wens")
btn_4 = Button(window, text='4', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
               command=lambda: add_digit(4))
btn_4.grid(column=0, row=3, stick="wens")
btn_5 = Button(window, text='5', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
               command=lambda: add_digit(5))
btn_5.grid(column=1, row=3, stick="wens")
btn_6 = Button(window, text='6', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
               command=lambda: add_digit(6))
btn_6.grid(column=2, row=3, stick="wens")
btn_minus = Button(window, text='-', bg='orange', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
                   command=lambda: add_digit('-'))
btn_minus.grid(column=3, row=3, stick="wens")
btn_1 = Button(window, text='1', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
               command=lambda: add_digit(1))
btn_1.grid(column=0, row=4, stick="wens")
btn_2 = Button(window, text='2', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
               command=lambda: add_digit(2))
btn_2.grid(column=1, row=4, stick="wens")
btn_3 = Button(window, text='3', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
               command=lambda: add_digit(3))
btn_3.grid(column=2, row=4, stick="wens")
btn_plus = Button(window, text='+', bg='orange', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
                  command=lambda: add_digit('+'))
btn_plus.grid(column=3, row=4, stick="wens")
btn_0 = Button(window, text='0', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=9,
               command=lambda: add_digit(0))
btn_0.grid(column=0, row=5, columnspan=2)
btn_dot = Button(window, text='.', bg='black', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
                 command=lambda: add_digit('.'))
btn_dot.grid(column=2, row=5, stick="wens")
btn_ravno = Button(window, text='=', bg='orange', fg='white', bd=3, font=('Comic Sans MS', 20), height=1, width=4,
                   command=lambda: RAVNO())
btn_ravno.grid(column=3, row=5, stick="wens")
window.mainloop()
