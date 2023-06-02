first_word = b'class'
second_word = b'function'
third_word = b'method'

list_of_words = [first_word, second_word, third_word]

for word in list_of_words:
    print("Тип: ", type(word), "Содержимое: ", word, "Длина:", len(word))