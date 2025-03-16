
print('Входные данные:')
num1 = int(input())
num2 = int(input())
min_num, max_num = min(num1, num2), max(num1,num2)

while max_num % min_num != 0: 
    min_num, max_num = (max_num % min_num), min_num 
            
NOD = min_num
NOK = int((num1 * num2) / NOD)  

print(f'Вывод программы: \nНОД введенных чисел: {NOD}\nНОК введенных чисел: {NOK}')