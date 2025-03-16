import random

alpha = True
lower = True
upper = True


data = input('Входные данные:\n').split()


if data[0].isdigit():
    alpha = False
    

elif data[0].islower():
    upper == False

    
elif data[0].isupper():
    lower == False

print(alpha, upper, lower)

random_pw = list(data[0])

while len(random_pw) < int(data[1]):
    if not alpha and not upper: 
        random_pw.append(chr(random.randint(65, 90)))
     
    elif not alpha and not lower:
        random_pw.append(chr(random.randint(97, 122)))
    
    elif alpha: 
        random_pw.append(chr(random.randint(48, 57)))
    
    else:
        random_pw.append(random.choice([chr(random.randint(49, 57)), chr(random.randint(65, 90)), chr(random.randint(97, 122))]))



    



random.shuffle(random_pw)

print(f'Вывод программы (один из возможных:)\n{"".join(random_pw)}')