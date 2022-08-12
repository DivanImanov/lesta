# Задание 1

'''
На языке Python реализовать алгоритм (функцию) определения четности целого числа, 
который будет аналогичен нижеприведенному по функциональности, но отличен по своей 
сути. Объяснить плюсы и минусы обеих реализаций.

        Python example:

        def isEven(value):
            return value % 2 == 0

'''


# Функция, в отличии от примера, возвращает строку 'Odd' или 'Even' вместо True/False. 
def even_or_odd(number):
    if number % 2 != 0:
        return 'Odd'
    return 'Even'

# Функция производит логическое умножение двоичных чисел, в результате чего возвращает True/False.
def isEven(number):
    return bool(not number & 1)

# Функция проверяет цифру из разряда единиц на наличие в списке чётных цифр.
def isEven2(number):
    return int(str(number)[-1]) in range(0, 10, 2)

# Вывод на экран
print('\nЧётность\n')
print(1, even_or_odd(1))
print(2, even_or_odd(2))
print('')
print(1, isEven(1))
print(2, isEven(2))
print('')
print(1, isEven2(1))
print(2, isEven2(2))