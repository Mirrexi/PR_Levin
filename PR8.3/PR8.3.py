print('Задание 1')


class Clock:  # Класс "Часы"
    def __init__(self):
        self.__hours = -1
        self.__minutes = -1
        self.__seconds = -1
        while self.__hours < 0 or self.__hours > 23:  # Вводим часы в правильном формате
            self.__hours = int(input('Введите часы в правильном формате: '))
        while self.__minutes < 0 or self.__minutes > 59:  # Вводим минуты в правильном формате
            self.__minutes = int(input('Введите минуты в правильном формате: '))
        while self.__seconds < 0 or self.__seconds > 59:  # Вводим секунды в правильном формате
            self.__seconds = int(input('Введите секунды в правильном формате: '))

    def get_hours(self):  # Инкапсуляция часов
        return self.__hours

    def get_minutes(self):  # Инкапсуляция минут
        return self.__minutes

    def get_seconds(self):  # Инкапсуляция секунд
        return self.__seconds

    def add_hours(self):  # Добавляем +1 час
        self.__hours += 1
        if self.__hours > 23:
            self.__hours = 0

    def add_minutes(self):  # Добавляем +1 минуту
        self.__minutes += 1
        if self.__minutes > 59:
            self.__minutes = 0
            self.add_hours()  # Добавляем +1 час если 59мин+1мин

    def add_seconds(self):  # Добавляем +1 секунду
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.add_minutes()  # Добавляем +1 минуту если 59сек+1сек

    def __str__(self):  # Функция, показывающая время
        return f'{self.__hours}:{self.__minutes}:{self.__seconds}'


def main():  # Основная функция
    clock = Clock()  # Создание часов
    print(clock)  # Показываем время
    choose = 0
    while choose != 'stop':  # Настройка часов
        choose = input('Выберите, к чему прибавить 1 (1 - Час|2 - Минута|3 - Секунда|stop - стоп): ')
        if choose == '1':
            clock.add_hours()
        if choose == '2':
            clock.add_minutes()
        if choose == '3':
            clock.add_seconds()
        print(clock)  # Показываем время


main()  # Вызов основной функции

print('Задание 2 (1)')


class Square:  # Создание класса Квадрата
    def __init__(self, side):
        self.side = side  # Сторона квадрата

    def S(self):  # Функция вычисления площади квадрата
        return (self.side * self.side)


class Circle:  # Создание класса Круга
    def __init__(self, radius):
        self.pi = 3.14
        self.radius = radius  # Радиус круга

    def S(self):  # Функция вычисления площади круга
        return (self.pi * self.radius ** 2)


class Rectangle:  # Создание класса Прямоугольника
    def __init__(self, side, other_side):
        self.side = side  # Сторона Прямоугольника
        self.other_side = other_side  # Другая сторона прямоугольника

    def S(self):  # Функция вычисления площади прямоугольника
        return (self.side * self.other_side)


S_Square = Square(5)  # Вычисление площади квадрата со стороной 5
S_Circle = Circle(3)  # Вычисление площади круга с радиусом 3
S_Rectangle = Rectangle(2, 3)  # Вычисление площади прямоугольника со сторонами 2 и 3
l = [S_Square, S_Circle, S_Rectangle]  # Записываем вычисленные площади в список
for i in l:
    print(i.S())  # Выводим значения площадей из полученного списка

print('Задание 2 (2)')


class Triangle:  # Создание класса Треугольника
    def __init__(self, side, height):
        self.side = side #Сторона треугольника
        self.height = height #Высота треугольника

    def S(self):  # Функция вычисления площади треугольника
        return (self.side * self.height * 0.5)


class Paral:  # Создание класса Параллелограмма
    def __init__(self, side, height):
        self.side = side #Сторона параллелограмма
        self.height = height #Высота к стороне параллелограмма

    def S(self):  # Функция вычисления площади параллелограмма
        return (self.side * self.height)


class Trapezoid:  # Создание класса Трапеции
    def __init__(self, side, other_side, height):
        self.side = side #Основание трапеции
        self.other_side = other_side #Другое основание трапеции
        self.height = height #Высота трапеции

    def S(self):  # Функция вычисления площади трапеции
        return ((self.side + self.other_side) * self.height * 0.5)


S_Triangle = Triangle(4, 3) # Вычисление площади треугольника со стороной 4 и высотой 3
S_Paral = Paral(7, 5) # Вычисление площади параллелограмма со стороной 7 и высотой 5
S_Trapezoid = Trapezoid(1, 3, 2) # Вычисление площади трапеции с основаниями 1 и 3, также высотой 2
l = [S_Triangle, S_Paral, S_Trapezoid] # Записываем вычисленные площади в список
for i in l:
    print(i.S())  # Выводим значения площадей из полученного списка
