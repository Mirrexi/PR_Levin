# Методы для строк
# 1) .replace - удаляет строку, заменив её
s = "test"
s = s.replace("test", "123")
print(s)
# 2) .lower() - преобразует все буквенные символы в строчные
print('.lower()', 'GoOd DaY', 'GoOd DaY'.lower())
# 3) .swapcase() - меняет регистр буквенных символов на противоположный
print('.swapcase()', 'good day', 'good day'.swapcase())
# 4) .title() - преобразует первые буквы всех слов в заглавные
print('.title()', 'good day', 'good day'.title())
# 5) .upper() - преобразует все буквенные символы в заглавные
print('.upper()', 'good day', 'good day'.upper())
# Методы для списков
# 1) .append(x) - добавляет элемент в конец списка
spisok = list('список')
spisok.append('а')
print(".append(x)", spisok)
# 2) .extend(L) - Расширяет список list, добавляя в конец все элементы списка L
spisok1 = list('да')
spisok2 = list('нет')
spisok1.extend(spisok2)
print('.extend(L)', spisok1)
# 3) .remove(x) - Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
spisok1.remove('т')
print('.remove(x)', spisok1)
# 4) .pop([i]) - Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
print('.pop()', spisok1.pop())
# 5) .count(x) - Возвращает количество элементов со значением x
print('.count(x)', spisok1.count('а'))
# Методы для словарей
# 1) .clear() - Очищает словарь
d = {'1': 'dict', '2': 'ionary'}
d.clear()
print('.clear()', d)
# 2) .keys() - возвращает ключи в словаре
d = {'1': 'dict', '2': 'ionary'}
print('.keys()', d.keys())
# 3) .items() - возвращает пары (ключ, значение).
print('.items()', d.items())
# 4) .values() - возвращает значения в словаре
print('.values()', d.values())
# 5) dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError
print('.popitem', d.popitem())
# Методы для кортежей
# 1) .count('l') - Возвращает количество раз, которое указанный элемент встречается в кортеже
kortej = tuple('hello, world!')
print('.count(l)', kortej.count('l'))
# 2) .index(e) - Ищет кортеж по указанному значению и возвращает его индекс
print('.index(e)', kortej.index('e'))
# 3) len() - определяет количество элементов кортежа
print('len()', len(kortej))
# 4) .__sizeof__() - возвращает размер кортежа в байтах
print('.__sizeof__()', kortej.__sizeof__())
# 5) =tuple() - создание пустого кортежа
kortej = tuple()
print('kortej=tuple()', kortej)
#Методы для файлов
#1) open() - открывает файл на компьютере
f=open('123.txt','w')
#2) .write() - запись в файл
f.write('Ya vso mogu')
#3) .close - закрывает файл
f.close()
#4) .read() - чтение файла
f=open('123.txt','r')
print(f.read(100))
#5) .readline() - построчное чтение файла
f.seek(0,0)
print(f.readline())
h=input()