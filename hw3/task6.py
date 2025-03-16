print('Входные данные:')
pw = str(input())


j=0

for i in pw:
    if i.isdigit(): j+=1


p = 0

for i in pw:
    if i.isalpha(): p+=1



pw_without_space = pw.replace(' ', '')

k = 0
for i in range(1, len(pw)):
    for z in range(i):
        if pw[i] == pw[z]:
            k += 1
            


if len(pw) < 10:
     print('Вы ввели недопустимый пароль')

elif pw.islower() == True:
    print('Вы ввели недопустимый пароль')

elif pw.isupper() == True:
    print('Вы ввели недопустимый пароль')

elif j == 0: 
    print('Вы ввели недопустимый пароль')

elif p == 0:
    print('Вы ввели недопустимый пароль')
  
elif len(pw) != len(pw_without_space):
    print('Вы ввели недопустимый пароль')

elif k != 0: 
    print('Вы ввели недопустимый пароль')

else:
    print('Вы ввели допустимый пароль')