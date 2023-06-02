list_of_words = ["разработка", "администрирование", "protocol", "standard"]

for word in list_of_words:
    word_encode = word.encode("utf-8")
    print("Байтовое представление: ", word_encode)
    print("Строковое представление:", word_encode.decode("utf-8"))
