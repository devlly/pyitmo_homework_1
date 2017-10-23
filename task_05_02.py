class CustomError(Exception):
    print('Точка лежит на оси!')


def get_quadrant_number(x, y):
    try:
        if x > 0 and y > 0 print('точка лежит в первой четверти')
        if x > 0 and y < 0 print('точка лежит в четвертой четверти')
        if x < 0 and y < 0 print('точка лежит в третьей четверти')
        if x < 0 and y > 0 print('точка лежит во второй четверти')
    except (ImportError, CustomError) as e:
        print(e)

    
