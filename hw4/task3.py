input_string = input('Входные данные:\n')


input_string = input_string.lower()
input_string = input_string.split()
input_string = [word.strip('.,!;()[]?') for word in input_string]


num_dict = { 'один' : 1, 'два' : 2, 'три' : 3, 'четыре' : 4, 'пять' : 5, 'шесть' : 6,  'семь' : 7, 'восемь' : 8, 'девять' : 9, 'десять' : 10, \
             'одиннадцать' : 11 , 'двенадцать' : 12 , 'тринадцать' : 13 , 'четырнадцать' : 14 , 'пятнадцать' : 15 , 'шестнадцать' : 16, \
             'семнадцать' : 17, 'восемнадцать' : 18, 'девятнадцать' : 19, 'двадцать' : 20 , 'ноль' : 0}


symbols =  ['плюс' , 'минус']


if input_string[1] == symbols[0]:
    result = num_dict[input_string[0]] + num_dict[input_string[2]]
    for key, value in num_dict.items():
        if num_dict[key] == result:
            print(key)


elif input_string[1] == symbols[1]:
    result = num_dict[input_string[0]] - num_dict[input_string[2]]
    for key, value in num_dict.items():
        if num_dict[key] == result:
            print(key)
    if result < 0:
            for key, value in num_dict.items():
                if num_dict[key] == abs(result):
                    print(f'минус {key}')





