list_of_words = ["сетевое программирование", "сокет", "декоратор"]
list_of_words = map (lambda x: x + '\n', list_of_words)

with open("test_file.txt", "w") as f:
          f.writelines(list_of_words)
          
file_open = open('test_file.txt', 'r', encoding="UTF-8")
for line in file_open:
        print(line)
file_open.close()
print(file_open.encoding)