print('Входные данные: ')
num1 = int(input())
num2 = int(input())

max1 = min2 = max (num1, num2)
min1 = max2 = min (num1, num2) 

num = int(input())
while True:
    if num == 0:
        break
    else:
        if max1 < num:
            max1, max2 = num, max1
        elif num > max2:
            max2 = num 
        if min1 > num:
            min1, min2 = num, min1
        elif num < min2: 
            min2 = num
    num = int(input())

print(f'Вывод программы: \n {max2} \n {min2}')


