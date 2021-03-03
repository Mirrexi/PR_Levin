import random


class Warrior:
    def __init__(self):
        self.hp = 100
        self.armor = 0

    def attack_damage(self):
        return random.randint(0, 10)  # Функция для рандомного урона


class Red(Warrior):
    def __init__(self):
        super().__init__()
        self.armor = 5


class Blue(Warrior):
    def __init__(self):
        super().__init__()
        self.armor = 3


def fight(first, second):  # Функция битвы
    while first.hp > 0 and second.hp > 0:
        damage = first.attack_damage() - second.armor  # Срез урона первого бронёй второго
        damage = damage if damage >= 0 else 0  # Чтобы не наносил отрицательный урон
        second.hp -= damage  # Нанесение урона второму
        print("The first one deals", damage, "damage" ' |', second.hp, 'the second ones hp left')
        if second.hp > 0:
            damage = second.attack_damage() - first.armor  # Срез урона второго бронёй первого
            damage = damage if damage >= 0 else 0  # Чтобы не наносил отрицательный урон
            first.hp -= damage  # Нанесение урона первому
            print("The second one deals ", damage, "damage" '|', first.hp, 'the first ones hp left')
    if first.hp <= 0:  # Проверка на смерть одного из соперников
        print('THE SECOND ONE WON')
    else:
        print('THE FIRST ONE WON')


fight(Red(), Blue())  # Вызов функции битвы
