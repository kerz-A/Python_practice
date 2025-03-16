example_text = set(input(f'Входные данные:\n').split())
user_text = set(input().split())

common_word = user_text.intersection(example_text)

percentage = round((1 - len(common_word)/len(user_text))*100)

print(f'Вывод программы:\n{len(common_word)}\n{int(percentage)}%') 