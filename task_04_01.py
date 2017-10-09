'''
Задача №1.
Файл "data.txt" заполнен случайными целыми числами, числа разделены одним пробелом.
1. Сформировать файл "out-1.txt" из элементов файла "data.txt", делящихся без остатка на n
2. Сформировать файл "out-2.txt" из элементов файла "data.txt", возведенных в степень p
n и p - целые числа, вводимые с клавиатуры.
Имя файла: task_04_01.py
Тестовый набор данных №1:
Содержимое файла data.txt: 48 48 3 75 26 57 53 21 71 15
Входные данные: 2 3
Содержимое файла out-1.txt: 48 48 26
Содержимое файла out-2.txt: 110592 110592 27 421875 17576 185193 148877 9261 357911 3375
'''
with open('data.txt') as f:
    content = f.read()

content = content.split(' ')
#content = content.replace(' ', '')
l = len(content)
#content = lst(content)
print('Введите n и p')
data = input()
data = data.split(' ')
n, p = int(data[0]), int(data[1])
i = 0
lst, lst1 = [], []

for i in range(l):
    if int(content[i]) % n == 0:
        lst.append(int(content[i]))
lst = str(lst)
lst = lst.replace(', ', ' ')
lst = lst.strip('[]')
with open('out-1.txt', 'w') as x:           
    x.write(lst)
    

for i in range(l):
    lst1.append(int(content[i]) ** p)
lst1 = str(lst1)
lst1 = lst1.replace(', ', ' ')
lst1 = lst1.strip('[]')
with open('out-2.txt', 'w') as y:
        y.write(lst1)


