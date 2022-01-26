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
import time
import threading

WAIT_TIME = 10
# global variables (shared among threads)
closed = False
messages_sent = 0


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


def send_loop(sock, serverAddr, auto):
    global closed, messages_sent

    if not auto:
        print('Digite "!quit" para encerrar o programa imediatamente.\n')

    for msgCounter in range(1, 31):
        # sending message
        msgToServer = None
        if auto:
            msgToServer = f"{msgCounter} >> Mensagem {msgCounter}"
        else:
            userMsg = input(f"Sua mensagem {msgCounter}: ")
            if userMsg == "!quit":
                sock.close()
                closed = True
                break
            msgToServer = f"{msgCounter} >> " + userMsg

        sock.sendto(bytes(msgToServer, "utf-8"), serverAddr)
        messages_sent += 1

        print(f"Mensagem {msgCounter} enviada.\n")

        if msgCounter % 10 == 0:  # after 10 messages, wait 10secs
            print("Esperando 10 segundos...\n")
            time.sleep(WAIT_TIME)
        # after 30 messages, wait 10secs (from above) and then quit
        if msgCounter == 30 or closed:
            sock.close()
            closed = True
            break


def recv_loop(sock, acked):
    global closed

    while True:
        # receiving ACKS
        try:
            ack, _ = sock.recvfrom(2048)

            ackNum = int(ack.decode("utf-8")[3:])
            acked[ackNum - 1] = True

            print(f"ACK {ackNum} recebido!\n")
        except:
            closed = True


def main():
    # socket config
    privateIP = get_private_IP()
    print(f"Seu endereço IPv4 privado é {privateIP}.\n")

    serverIP = input("Digite o endereço IPv4 público do server: ")
    serverAddr = (serverIP, 60000)

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.bind((privateIP, 0))  # gets a random available port

    acked = [False for _ in range(30)]

    auto = input("Mandar mensagens automaticamente? (S/N) \n") == "S"

    sl_thread = threading.Thread(
        target=send_loop,
        args=(clientSocket, serverAddr, auto),
        daemon=True)

    rl_thread = threading.Thread(
        target=recv_loop,
        args=(clientSocket, acked),
        daemon=True)

    rl_thread.start()
    sl_thread.start()

    sl_thread.join()

    if messages_sent:
        taxa = 1 - sum(acked) / messages_sent
    else:
        taxa = "-"
    print(f"Taxa de perda: {taxa}.")

    print("\nAdeus.")


if __name__ == "__main__":
    main()
