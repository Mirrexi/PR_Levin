import os

print('Задание 1')


def Directory_content(dir):
    print("Все папки и файлы:", os.listdir(dir))


dir = input("Введите директорию: ")
Directory_content(dir)

print()
print('Задание 2')


def Read_txt(file, separator):
    if separator:
        separator = separator
    else:
        separator = '\n'
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read().split(separator)
    print(f'Содержимое текстового документа: {content}')


file = input('Введите директорию .txt файла: ')
separator = input('По какому разделителю будет разделён текст? ')
Read_txt(file, separator)

print()
print('задание 3')


def Record():
    text = input('Введите текст для записи: ')
    with open('file.txt', 'a+', encoding='utf-8') as f:
        if f.tell():
            f.write(f'\n\n{text}')
        else:
            f.write(text)


Record()

print()
print("Задание 4")


def Marks():
    average = 0
    directory = input('Введите директорию txt файла: ')
    with open(directory, 'r', encoding='utf-8') as f:
        students = f.read().splitlines()
    print(students)
    for i in students:
        mark = int(i[-1])
        average += mark
        if mark < 3:
            print(i)
    average /= len(students)
    print(f'Средний балл класса: {average}')


Marks()

print()
print('Задание 5')


def Score():
    directory = input('Введите директорию txt файла: ')
    with open(directory, 'r', encoding='utf-8') as f:
        stroki = f.read().splitlines()
    print(f'Количество строк: {len(stroki)}')
    for i in stroki:
        print(f'Строка: {i}')
        print(f'Количество символов: {len(i)}')
        print(f'Количество слов: {len(i.split(" "))}')
        print()


Score()
