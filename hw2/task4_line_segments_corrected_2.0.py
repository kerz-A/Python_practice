print('Входные данные:')
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

if x2 < y1 or x1 > y2: 
    print('Отрезки не пересекаются')

elif x1 == y2: 
    print(f'Отрезки пересекаются в точке {x1}')

elif x2 == y1: 
    print(f'Отрезки пересекаются в точке {x2}')

else:
    print(f'Длина пересечения отрезков {min(x2, y2) - max (x1, y1)}')