'''
Задача №4. Закрепляем математические операторы
Напишите программу, предлагающую пользователю ввести три вершины.
Координаты X и Y (2 числа), заданы как целые числа, т.е. int.
Нужно определить является ли треугольник, с указанными координатами, прямоугольным.
В решении использовать только математические и логические операторы.
В вычислениях запрещено(!!!) переходить в дробные числа.
Результат работы программы одно из слов:
»> Прямоугольный
»> Не прямоугольный
Имя файла: task_01_04.py
Входные данные: 2 7 6 1 12 5
Выходные данные: Прямоугольный'''

print('введите координаты вершин')
vertex = input()
vertex = vertex.split(' ')

x1, y1, x2, y2, x3, y3 = int(vertex[0]), int(vertex[1]), int(vertex[2]), int(vertex[3]), int(vertex[4]), int(vertex[5])

st1 = (x1 - x2)**2 + (y1 - y2)**2
st2 = (x1 - x3)**2 + (y1 - y3)**2
st3 = (x3 - x2)**2 + (y3 - y2)**2

if st1 > st2 and st1 > st3:
    if st1 == st2 + st3:
        print('Прямоугольный')
    else:
        print('Не прямоугольный')

if st2 > st1 and st2 > st3:
    if st2 == st1 + st3:
        print('Прямоугольный')
    else:
        print('Не прямоугольный')

if st3 > st2 and st3 > st1:
    if st3 == st2 + st1:
        print('Прямоугольный')
    else:
        print('Не прямоугольный')
