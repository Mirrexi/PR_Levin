trX = int(input("Введите координату X для клада: "))
trY = int(input("Введите координату Y для клада: "))
X, Y = 0, 0  # Наше местонахождение
dirX, dirY = 0, 1  # Наше направление взгляда
move = 0
dir = [[0, 1, "Север"], [1, 0, "Восток"], [0, -1, "Юг"], [-1, 0, "Запад"]]
dirpoint = 0
act = str(input('Введите действие: '))
while act != 'стоп':
    if act not in ['вперёд', 'налево', 'направо', 'разворот', 'стоп']:  # Проверка на правильное написание команд
        act = str(input('Введите действие: '))
        continue
    if act == 'вперёд':
        step = int(input("Введите количество шагов: "))
        X, Y = X + dirX * step, Y + dirY * step  # Передвижение на step шагов
        move += 1
        act = str(input('Введите действие: '))
        continue
    elif act == 'налево':
        dirpoint -= 1
    elif act == 'направо':
        dirpoint += 1
    elif act == 'разворот':
        dirpoint += 2
    dirX, dirY = dir[dirpoint % 4][0], dir[dirpoint % 4][1]  # Поворот, в зависимости от команды
    move += 1
    act = str(input('Введите действие: '))
print(F"Количество совершённых ходов: {move}\nНаше направление: {dir[dirpoint][2]}")
