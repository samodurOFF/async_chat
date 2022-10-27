from socket import *
import json
from variables import *


def answer(msg_from_client):
    if msg_from_client['action'] == PRESENCE:
        return RESPONSE_200


def init_socket():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(((DEFAULT_IP_ADDRESS, DEFAULT_PORT)))
    sock.listen()
    return sock


def start_server():
    sock = init_socket()
    print(dir(sock))
    print(sock)
    print(sock.getsockname())
    while True:
        client, addr = sock.accept()
        answer_to_client = answer(json.loads(client.recv(MAX_PACKAGE_LENGTH)))
        client.send(json.dumps(answer_to_client, sort_keys=True, indent=4).encode(ENCODING))


if __name__ == '__main__':
    start_server()
