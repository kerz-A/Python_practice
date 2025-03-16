
print('Входные данные:')
num1 = int(input())
num2 = int(input())
min_num, max_num = min(num1, num2), max(num1,num2)

while min_num !=0:
        if (max_num % min_num) == 0:
            break 
        else:
            min_num, max_num = (max_num % min_num), min_num 
            
NOD = min_num
  

max_num = max(num1,num2)
while True:
    if (max_num % num1 == 0) and (max_num % num2 == 0):
        NOK = max_num
        break
    max_num +=1

print(f'Вывод программы: \nНОД введенных чисел: {NOD}\nНОК введенных чисел: {NOK}')