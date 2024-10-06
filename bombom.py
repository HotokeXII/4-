#ЛАБА №4
#1.импорт стандартных модулей
'''import math
x = int(input('введите число: '))
print('квадратный корень: ', math.sqrt(x))'''

#2.создание и использование собственного модуля
'''import my_module
x = int(input('введите первое число: '))
y = int(input('введите второе число: '))
print(my_module.plus(x, y))'''

#3.создание и использование пакетов
import my_module
x = int(input('введите первое число: '))
y = int(input('введите второе число: '))
z = input('выберите операцию: ')
if z == 'сложение':
    print(my_module.plus(x, y))
elif z == 'умножение':
    print(my_module.umn(x, y))
elif z == 'деление':
    print(my_module.delit(x, y))
else:
    print('такой операции нет')