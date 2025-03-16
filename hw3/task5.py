print('Входные данные:')
xy = [int(num) for num in input().split(' ')]
wz = [int(num) for num in input().split(' ')]


prod1 = []

prod2 = []

for i in range(xy[0], xy[1]+1):
    prod1.append(i)

for i in range(wz[0], wz[1]+1):
    prod2.append(i)

print('        ', end = '')

for i in prod2:
    print(f'       {i}', end = '')

for i in range(len(prod1)):
    print(f'\n       {prod1[i]}', end = '')   
    for j in range(len(prod2)):
        if (prod1[i]*prod2[j]) // 10 != 0:
            print(f'      {prod1[i]*prod2[j]}', end = '')
        else:
            print(f'       {prod1[i]*prod2[j]}', end = '')

