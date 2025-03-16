
seq = [int(num) for num in input('Входные данные \n').split(' ')]

j=0

for i in range(1, len(seq) - 1):
    if (seq[i] > seq [i+1]) and (seq[i] > seq [i-1]):
        j+=1
    
print(f'Вывод программы \n {j}')