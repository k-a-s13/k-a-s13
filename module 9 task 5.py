print('Задача 5. Марсоход 2')
x = 8
y = 10
while True:
    print('[Программа]: Марсоход находится на позиции ', x, y)
    move = input('[Оператор]: ')
    if move == 'w' and y < 20:
        y += 1
    elif move == 's' and y > 0:
        y -= 1
    elif move == 'a' and x > 0:
        x -= 1
    elif move == 'd' and x < 15:
        x += 1
    else:
        print('Поворачивай ты уперся в стену!')
