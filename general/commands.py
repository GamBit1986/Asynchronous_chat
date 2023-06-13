import json
import time

from general.variables import MAX_PACKAGE_LENGHT, ENCODING, ACCOUNT_NAME, ACTION, TIME, USER, PRESENCE


def get_message(socket):
    encoded_responce = socket.recv(MAX_PACKAGE_LENGHT)
    if isinstance(encoded_responce, bytes):
        json_responce = encoded_responce.decode(ENCODING)
        responce = json.loads(json_responce)
        if isinstance(responce, dict):
            return responce
        raise ValueError
    raise ValueError


def send_message(socket, message):
    json_massage = json.dumps(message)
    encoded_massage = json_massage.encode(ENCODING)
    socket.send(encoded_massage)


def create_presence(account_name="GUEST"):
    out = {
        ACTION: PRESENCE, TIME: time.time(), USER: {ACCOUNT_NAME: account_name}
    }
    return out


def create_answer(account_name="SERVER"):
    out = {
        ACTION: PRESENCE, TIME: time.time(), USER: {ACCOUNT_NAME: account_name}
    }
    return out
