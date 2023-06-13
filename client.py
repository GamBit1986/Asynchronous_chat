# Программа клиента для отправки приветствия серверу и получения ответа
from socket import *
import time

from general.variables import DEFAULT_PORT, DEFAULT_IP, ENCODING, PRESENCE, TIME, ACCOUNT_NAME, ACTION, USER, RESPONSE, ERROR, MAX_PACKAGE_LENGHT
from general.commands import send_message, get_message, create_presence


s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP

s.connect((DEFAULT_IP, DEFAULT_PORT))
msg = create_presence()
send_message(s, msg)
data = get_message(s)

print('Сообщение от сервера: ', data, ', длиной ', len(data), 'байт')
s.close()
