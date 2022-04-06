import socket
import threading


class Client():
    def __init__(self,nickname,address,port):
        self.nickname = nickname
        self.address = address
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """nickname = input("Choose a nickname : ")
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1',9184))
    """
    def connect(self):
        self.client.connect((self.address,self.port))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == "nickname?":
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("an error has occured!")
                self.client.close()
                break


    def write(self):
        while True:
            message = f'{self.nickname}: {input("")}'
            self.client.send(message.encode('ascii'))
            

if __name__ == "__main__":
           
    nickname = input("choose a nickname:")
    #port = int(input("choose a port:"))
    #host = input("choose a host:")
    port = 9900
    host = "127.0.0.1"
    commande = input(f"Enter CONNECT {host} {port} to connect yourself:")
    if commande.upper() == f"CONNECT {host} {port}":
    
        client = Client(nickname,host,port)
        client.connect()
        receive_thread = threading.Thread(target=client.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=client.write)
        write_thread.start()
    
    else:
        print(f"Failed to connect")
