list_of_words = ["разработка", "сокет", "декоратор"]

for word in list_of_words:
    print(word, type(word))
    unicode_word = word.encode("utf-8")
    print("вид в байтах закодированного в Юникоде слова: ",
          unicode_word, type(unicode_word))
