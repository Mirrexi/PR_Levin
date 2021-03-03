print('Задание 1')
def kv_ur(a, b, c):
    D = b * b - 4 * a * c
    if D<0:
        print('Нет корней...')
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2


try:
    a=int(input('Введите значение переменной a: '))
    b=int(input('Введите значение переменной b: '))
    c=int(input('Введите значение переменной c: '))
    print(kv_ur(a, b, c))
except ZeroDivisionError:
    print('А на ноль делить нельзя...')
except TypeError:
    print('А буквы вводить то нельзя...')
print('ok')

print('Задание 2')


def dlina(stroka):
    return len(stroka)


stroka = input('Введите строку десяти или меньше символов: ')
try:
    print(dlina(stroka))
    print(f' Десятый символ: {stroka[10]}')
except IndexError:
    print('А десятого символа то нет...')
print('ok')

print('')

print('Задание 3')
class Kto:
    def __init__(self, kto):
        self.kto = kto

method=str(input('Введите название искомого метода: '))
try:
    print(Kto.method(5))
except AttributeError:
    print('А такого метода то нет...')
print('ok')

print('')

print('Задание 4')
print('А всё уже сделано...')

print('')

print('Задание 5')
try:
    raise IndexError
except IndexError:
    print('IndexError')

print('')

print('Задание 6')
class NegValException(Exception):
   pass

try:
   val = int(input("input positive number: "))
   if val < 0:
       raise NegValException("Neg val: " + str(val))
   print(val)
except ValueError:
    print('А нужно число вводить...')
except NegValException as e:
    print(e)