print('Входные данные')
num = int(input())
base = int(input())
result = []
result.append(num % base)

while num >= base:
    num = num // base
    temp = (num % base)
    result.append(temp)

changelist = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(len(result)):
    if result[i] >= 10:
        temp = result[i] - 10
        result[i] = changelist[temp] 

final_result = (''.join(map(str, result[::-1])))
print(f'Вывод программы \n{final_result}')  