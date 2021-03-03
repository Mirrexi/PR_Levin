import random

print('Задача 1')


class Counter:  # Класс "Счётчик" с полной инкапсуляцией
    __k = 0

    def add(self):
        self.__k += 1

    def get(self):
        return self.__k

    def clear(self):
        self.__k = 0

    def __str__(self):
        return str(self.__k)


a = Counter()  # Создание счётчика
print(a)  # Вывод счётчика (0)
a.add()  # Прибавляем к счётчика единицу
print(a)  # Вывод счётчика (1)

input()

print('Задача 2')


class Cow:  # Класс "Корова"
    def __init__(self):
        self.__hungered = 100  # Изначальная сытость коровы

    def getHungred(self):  # Инкапсуляция сытости коровы
        return self.__hungered

    def eat(self, grass):  # Прибавление пищевой ценности травы к сытости коровы
        self.__hungered += grass.getHunger()

    def isHungry(self):  # Проверяем, голодна ли корова
        return self.__hungered < 90

    def tact(self):  # Корова постепенно голодает
        self.__hungered -= random.randint(2, 7)

    def isAlive(self):  # Проверяем, жива ли ещё корова
        return self.__hungered > 1


class Grass:  # Класс "Трава"
    def __init__(self, hunger):
        self.__hunger = hunger

    def getHunger(self):  # Инкапсуляция пищевой ценности травы
        return self.__hunger


def main():  # Основная функция
    cow = Cow()  # Создание коровы

    print("Корова вышла на полянку...")

    while cow.isAlive():  # Корова будет есть и голодать пока жива
        cow.tact()

        print(f"Корова проголодалась до {cow.getHungred()}%")

        if cow.isHungry() and cow.isAlive():
            grass = Grass(random.randint(1, 5))  # Корова находит траву со случайной пищевой ценностью
            cow.eat(grass)  # Корова ест траву
            print(f"Корова покушала траву и восстановила {grass.getHunger()} голода до {cow.getHungred()}")

    print("Корова умерла от голода. Светлая память")


main()  # Вызов основной функции

input()

print('Задача 3')


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
