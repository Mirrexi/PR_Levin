from tkinter import *
from tkinter import messagebox
import os


def Vivod1():
    try:
        vivod1.configure(text=f"Содержимое директории: {os.listdir(dir1.get())}")
    except Exception:
        messagebox.showinfo('ERROR', 'Неправильная директория')
        dir1.delete(0, END)


def Read_txt():
    separator = sep2.get()
    if sep2.get():
        separator = separator
    else:
        separator = '\n'
    with open(dir2.get(), 'r', encoding='utf-8') as f:
        content = f.read().split(separator)
    return content


def Vivod2():
    try:
        vivod2.configure(text=f"Содержимое текстового документа: {Read_txt()}")
    except Exception:
        messagebox.showinfo('ERROR', 'Неправильная директория')
        dir1.delete(0, END)


def Record():
    text = vvod3.get()
    with open('file.txt', 'a+', encoding='utf-8') as f:
        if f.tell():
            f.write(f'\n\n{text}')
            vivod3.configure(text='Готово!')
        else:
            f.write(text)
            vivod3.configure(text='Готово!')


def Marks():
    average = 0
    bad_students = []
    directory = dir4.get()
    with open(directory, 'r', encoding='utf-8') as f:
        students = f.read().splitlines()
    vivod4.configure(text=f'Все учащиеся класса: {students}')
    for i in students:
        mark = int(i[-1])
        average += mark
        if mark < 3:
            bad_students.append(i)
        vivod4_2.configure(text=f'Учащиеся с плохой успеваемостью: {bad_students}')
    average /= len(students)
    vivod4_3.configure(text=f'Средний балл класса: {average}')


def Score():
    directory = dir5.get()
    with open(directory, 'r', encoding='utf-8') as f:
        stroki = f.read().splitlines()
    vivod5.configure(text=f'Количество строк: {len(stroki)}')
    s = ''
    for i in stroki:
        s += f'Строка: {i}; Количество символов: {len(i)}; Количество слов: {len(i.split(" "))};\n'
    vivod5_2.configure(text=s)


window = Tk()
window.title('Интерфейс')
window.geometry('1700x1000')

# Задание 1
ex1 = Label(window,
            text='Задание 1. Реализовать функцию, которая находит и выводит на экран все папки и файлы в указной директории. Путь к директории вводится пользователем.',
            font=('Comic Sans ms', 12))
ex1.grid(column=0, row=0, stick='w')
ex1_2 = Label(window, text='Введите директорию, содержимое которой Вы хотите найти:', font=('Comic Sans ms', 10))
ex1_2.grid(column=0, row=1, stick='w')
dir1 = Entry(window, width=100, font=('Comic Sans ms', 10))
dir1.grid(column=0, row=2, stick='w')
btn1 = Button(window, text='Найти', bg='black', fg='white', font=('Comic Sans ms', 10), command=lambda: Vivod1())
btn1.grid(column=0, row=3, stick='w')
vivod1 = Label(window, text='', font=('Comic Sans ms', 10))
vivod1.grid(column=0, row=4, stick='w')

# Задание 2
ex2 = Label(window,
            text='Задание 2. Реализовать функцию, которая читает данные из файла формата .txt и преобразует их в список, разделяя текст по заданному пользователю разделителю.',
            font=('Comic Sans ms', 12))
ex2.grid(column=0, row=5, stick='w')
ex1_2 = Label(window, text='Введите директорию, в которой находится .txt файл:', font=('Comic Sans ms', 10))
ex1_2.grid(column=0, row=6, stick='w')
ex1_3 = Label(window, text='Введите разделитель, по которому будет разделён текст:', font=('Comic Sans ms', 10))
ex1_3.grid(column=0, row=8, stick='w')
dir2 = Entry(window, width=100, font=('Comic Sans ms', 10))
dir2.grid(column=0, row=7, stick='w')
sep2 = Entry(window, width=100, font=('Comic Sans ms', 10))
sep2.grid(column=0, row=9, stick='w')
btn2 = Button(window, text='Преобразовать', bg='black', fg='white', font=('Comic Sans ms', 10),
              command=lambda: Vivod2())
btn2.grid(column=0, row=10, stick='w')
vivod2 = Label(window, text='', font=('Comic Sans ms', 10))
vivod2.grid(column=0, row=11, stick='w')

# Задание 3
ex3 = Label(window,
            text='Задание 3.  Реализовать функцию, которая запрашивает у пользователя текст и записывает его в файл. При повторном вводе текста он должен добавляться к уже существующему через пустую строку.',
            font=('Comic Sans ms', 12))
ex3.grid(column=0, row=12, stick='w')
ex3_2 = Label(window, text='Введите текст для записи в файл:', font=('Comic Sans ms', 10))
ex3_2.grid(column=0, row=13, stick='w')
vvod3 = Entry(window, width=100, font=('Comic Sans ms', 10))
vvod3.grid(column=0, row=14, stick='w')
btn3 = Button(window, text='Записать', bg='black', fg='white', font=('Comic Sans ms', 10), command=lambda: Record())
btn3.grid(column=0, row=15, stick='w')
vivod3 = Label(window, text='', font=('Comic Sans ms', 10))
vivod3.grid(column=0, row=16, stick='w')

# Задание 4
ex4 = Label(window,
            text='Задание 4.  В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу. ',
            font=('Comic Sans ms', 12))
ex4.grid(column=0, row=17, stick='w')
ex4_2 = Label(window, text='Введите директорию txt файла:', font=('Comic Sans ms', 10))
ex4_2.grid(column=0, row=18, stick='w')
dir4 = Entry(window, width=100, font=('Comic Sans ms', 10))
dir4.grid(column=0, row=19, stick='w')
btn4 = Button(window, text='Вывести', bg='black', fg='white', font=('Comic Sans ms', 10), command=lambda: Marks())
btn4.grid(column=0, row=20, stick='w')
vivod4 = Label(window, text='', font=('Comic Sans ms', 10))
vivod4.grid(column=0, row=21, stick='w')
vivod4_2 = Label(window, text='', font=('Comic Sans ms', 10))
vivod4_2.grid(column=0, row=22, stick='w')
vivod4_3 = Label(window, text='', font=('Comic Sans ms', 10))
vivod4_3.grid(column=0, row=23, stick='w')

# Задание 5
ex5 = Label(window,
            text='Задание 5. В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.',
            font=('Comic Sans ms', 12))
ex5.grid(column=0, row=24, stick='w')
ex5_2 = Label(window, text='Введите директорию txt файла:', font=('Comic Sans ms', 10))
ex5_2.grid(column=0, row=25, stick='w')
dir5 = Entry(window, width=100, font=('Comic Sans ms', 10))
dir5.grid(column=0, row=26, stick='w')
btn5 = Button(window, text='Определить', bg='black', fg='white', font=('Comic Sans ms', 10), command=lambda: Score())
btn5.grid(column=0, row=27, stick='w')
vivod5 = Label(window, text='', font=('Comic Sans ms', 10))
vivod5.grid(column=0, row=28, stick='w')
vivod5_2 = Label(window, text='', font=('Comic Sans ms', 10))
vivod5_2.grid(column=0, row=29, stick='w')
window.mainloop()
