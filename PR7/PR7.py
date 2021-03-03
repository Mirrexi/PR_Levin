class car:
    def __init__(self, model, color):  # Конструктор
        self.wheels = 4
        self.model = model
        self.color = color
        print('Машина создана')

    def __str__(self):  # "Волшебный" метод str
        return f'{self.wheels} wheels, {self.model} model, {self.color} color'

    def __del__(self):  # Деструктор
        print('Машина удалена')


some_car = car('Lada', 'Red')
print(some_car)
del some_car

print('-------------------------------------')


class hat:
    def __init__(self, size, cost, color):  # Конструктор
        self.size = size
        self.cost = cost
        self.color = color
        print('There is your hat _П_')

    def __repr__(self):  # "Волшебный" метод repr
        return f'It is a {self.size}, {self.cost}, {self.color} hat'

    def __del__(self):  # Деструктор
        print('You have no hat anymore :(')


some_hat = hat('big', 'expensive', 'black')
print(some_hat)
del some_hat

print('-------------------------------------')


class money:
    def __init__(self, gold, silver, copper):  # Конструктор
        self.gold = gold
        self.silver = silver
        self.copper = copper

    def __add__(self, other):  # "Волшебный" метод add
        return f'You have {self.gold + other.gold} gold coins, {self.silver + other.silver} silver coins, {self.copper + other.copper} copper coins'  # Сложение содержимого мешков с монетами

    def normalize(self):  # Нормализация монет (100 copper --> 1 silver|100 silver --> 1 gold)
        if self.copper >= 100:
            self.silver += self.copper // 100
            self.copper %= 100
        if self.silver >= 100:
            self.gold += self.silver // 100
            self.silver %= 100

    def __del__(self):  # Функция деструкции
        print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')


bag1 = money(20, 2000, 10)
bag1.normalize()  # Нормализация первого мешка
bag2 = money(10, 10, 10)
bag2.normalize()  # Нормализация второго мешка
print(bag1 + bag2)  # Вывод суммы содержимого мешков
del bag1
del bag2
