input_text = input('Входные данные:\n')

input_text = input_text.split()

uniq_words = []
word_count = dict()


uniq_words = set(input_text)

print(f'Вывод программы:\nВ вашем тексте {len(uniq_words)} различных слов')


for word in uniq_words:
    word_count[word] = input_text.count(word)


print('Вывод программы:')


for word in word_count:
    print(f'Слово {word} встретилось в вашем тексте {word_count[word]} раз')


