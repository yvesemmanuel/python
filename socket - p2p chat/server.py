"""
Equipe:
- José Gabriel Pereira Tavares
- Eduardo Geber de Melo Albuquerque
- Emanuel Vinícius Tavares dos Santos Gomes
- Yves Emmanuel Francisco do Ó
- Antonio Bento de Souza Neto
- Felipe Guimaraes Vasconcelos
"""

import socket
import threading
import requests

# socket config
PORT = 60000


def get_private_IP():
    # credits: https://stackoverflow.com/a/28950776
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def get_public_IP():
    # credits: https://pytutorial.com/python-get-public-ip
    return requests.get('https://api.ipify.org/?format=json').json()['ip']


def close_on_enter(sock):
    input("Aperte Enter a qualquer momento para desligar o servidor.\n\n")
    sock.close()


def main():
    privateIP = get_private_IP()
    print("O endereço IPv4 privado do server é " + privateIP + "\n")

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((privateIP, PORT))

    publicIP = get_public_IP()
    print(f"O servidor está online em ({publicIP}, {PORT}).")

    close_thread = threading.Thread(
        target=close_on_enter,
        args=(serverSocket,),
        daemon=True)

    close_thread.start()

    while True:  # functioning of the server
        # receiving message
        try:
            data, clientAddr = serverSocket.recvfrom(2048)
        except OSError as e:
            print(e)
            break

        msgCounter, clientMessage = data.decode("utf-8").split(" >> ")

        # sending ACKS
        msgToClient = f"ACK{msgCounter}"
        try:
            serverSocket.sendto(bytes(msgToClient, "utf-8"), clientAddr)
        except OSError as e:
            print(e)
            break

        print(
            f'Respondendo a mensagem {msgCounter} de {clientAddr}: "{clientMessage}".')

    print("Servidor offline. Adeus.\n")


if __name__ == "__main__":
    main()
