# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import time

from general.variables import ENCODING, DEFAULT_PORT, DEFAULT_IP, MAX_CONNECTIONS, MAX_PACKAGE_LENGHT
from general.commands import send_message, get_message, create_answer

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind((DEFAULT_IP, DEFAULT_PORT))  # Присваивает порт 7777
s.listen(MAX_CONNECTIONS)  # Переходит в режим ожидания запросов;
# Одновременно обслуживает не более
# 5 запросов.
while True:
    client, addr = s.accept()
    data = get_message(client)
    print('Сообщение: ', data, ', было отправлено клиентом: ',
          addr)
    msg = create_answer()
    send_message(client, msg)

    client.close()
