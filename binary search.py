N = (100 + 1) // 2
left = 1
right = 100
while True:
 N = (left + right) // 2
 print('Твое число равно, меньше или больше, числа', N, '?')
 answer = int(input('1 - равно, 2 - больше, 3 - меньше: '))
 if answer == 1:
   print('Я угадал, молодец!')
   break
 elif answer == 2:
   left = N + 1
 else:
   right = N - 1
