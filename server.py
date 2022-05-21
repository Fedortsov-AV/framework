from select import select
from socket import socket, AF_INET, SOCK_STREAM

server_socket = socket(AF_INET, SOCK_STREAM)
srv_addres = ('127.0.0.1', 8035)

with server_socket as s:
    s.bind(srv_addres)
    s.listen(5)
    clients = []

    while True:
        wait: int = 0
        write: list = []
        read: list = []
        error: list = []

        print('Сервер запущен')
        try:
            client, addres = server_socket.accept()
        except Exception as e:
            print(f'Exeption {e} in accept')
        else:
            clients.append(client)

        try:
            read, write, error = select(clients, clients, clients, wait)
        except OSError as e:
            print(f'Exeption {e} in select')

        if read:
            for s_client in read:
                try:
                    data = s_client.recv(1024)
                    print(f'от {s_client} получено сообщение {data}')
                except Exception:
                    clients.remove(s_client)
        if write:
            for s_client in write:
                try:
                    message = b'hello'
                    s_client.send(message)
                except Exception:
                    pass
                clients.remove(s_client)





