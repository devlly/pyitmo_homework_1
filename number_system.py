'''Задача №2.
Реализуйте модуль number_system для перевода числа из одной системы счисления в другую.
Модуль должен содержать 6 функций для перевода из десятичной системы счисления в двоичную, восьмеричную, шестнадцатиричную и наоборот:
- dec2bin(number) - возвращает str
- dec2oct(number) - возвращает str
- dec2hex(number) - возвращает str
- bin2dec(number) - возвращает int
- oct2dec(number) - возвращает int
- hex2dec(number) - возвращает int

(!) Запрещено использовать встроенные функции/методы, решающие эту задачу.
Подсказка. Не спешите писать 6 разных реализаций, подумайте, можно ли написать универсальный алгоритм перевода.
В решении не должно присутствовать операций ввода-вывода.
Ситуации, когда в исходном числе есть не допустимые цифры (буквы), игнорируются.

Материал по переводу из одной СС в другую
http://inf.e-alekseev.ru/text/Schisl_perevod.html

Имя файла: number_system.py
Тестовый набор данных №1:
Входные данные: 250
Выходные данные для функций dec*: "11111010" "372" "FA"
Тестовый набор данных №2:
Входные данные: "1010011010"
Выходные данные: 666
Тестовый набор данных №3:
Входные данные: "755"
Выходные данные: 493
Тестовый набор данных №4:
Входные данные: "ABCDEF"
Выходные данные: 11259375'''

def dec2bin(number):
    st = 2
    n = st - 1
    lst = []
    number = int(number)
    while number//st >= n:
        lst.append(str(number%st))
        number = number//st
    lst.append(str(number%st))
    #lst.append(str(number//st))
    lst.reverse()
    transfert_dec2bin = ''.join(lst)
    return transfert_dec2bin

def dec2oct(number):
    st = 8
    n = st - 1
    lst = []
    number = int(number)
    while number//st >= n:
        lst.append(str(number%st))
        number = number//st
    lst.append(str(number%st))
    lst.append(str(number//st))
    lst.reverse()
    transfert_dec2oct = ''.join(lst)
    return transfert_dec2oct

def dec2hex(number):
    st = 16
    n = st - 1
    lst = []
    number = int(number)
    while number//st >= n:
        lst.append(str(number%st))
        number = number//st
    lst.append(str(number%st))
    #lst.append(str(number//st))
    lst = lst[::-1]
    strip = ''.join(lst)
    transfert_dec2hex = str(lst)
    transfert_dec2hex = transfert_dec2hex.replace('10', 'A')
    transfert_dec2hex = transfert_dec2hex.replace('11', 'B')
    transfert_dec2hex = transfert_dec2hex.replace('12', 'C')
    transfert_dec2hex = transfert_dec2hex.replace('13', 'D')
    transfert_dec2hex = transfert_dec2hex.replace('14', 'E')
    transfert_dec2hex = transfert_dec2hex.replace('15', 'F')
    transfert_dec2hex.replace(', ', '')    
    return transfert_dec2hex


def bin2dec(number):
    number = str(number)
    l = len(number)
    index = l - 1
    i, t = 0, 0
    st = 2
    for i in range(l):
        cypher = int(number[i])*(st**(index))
        index -= 1
        t += cypher
    transfer_bin2dec = t
    return transfer_bin2dec


def oct2dec(number):
    number = str(number)
    l = len(number)
    index = l - 1
    i, t = 0, 0
    st = 8
    for i in range(l):
        cypher = int(number[i])*(st**(index))
        index -= 1
        t += cypher
    transfer_oct2dec = t
    return transfer_oct2dec



def hex2dec(number):
    number = str(number)
    l = len(number)
    index = l - 1
    i, t = 0, 0
    st = 16
    for i in range(l):
        A = number[i]
        if number[i] == 'A': A = 10
        if number[i] == 'B': A = 11
        if number[i] == 'C': A = 12
        if number[i] == 'D': A = 13
        if number[i] == 'E': A = 14
        if number[i] == 'F': A = 15
        cypher = int(A)*(st**(index))
        index -= 1
        t += cypher
    transfer_hex2dec = t
    return transfer_hex2dec





