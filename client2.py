from ast import While
import socket
import threading


class Client():
    def __init__(self,nickname,address,port):
        self.nickname = nickname
        self.address = address
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   
    def connect(self):
        self.client.connect((self.address,self.port))

    def receive(self):
        boo = True
        while boo:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == "nickname?":
                    self.client.send(self.nickname.encode('utf-8'))

                #elif message == f"{self.nickname} is already taken press Enter to choose another nickname":

                while message == f"{self.nickname} is already taken press Enter to choose another nickname":

                    print(message)
                    self.nickname = input("choose another nickname:")
                    self.client.send(self.nickname.encode())
                    message = self.client.recv(1024).decode('ascii')


                #message = self.client.recv(1024).decode()
                if message.startswith("4") or message.startswith("2"):
                    print(message)

            except KeyboardInterrupt:
                print("an error has occured!")
                self.client.close()
                break


    def write(self):
        while True:
            message = f'{self.nickname}: {input("")}'
            self.client.send(message.encode('ascii'))
            



if __name__ == "__main__":
          
    
    #port = int(input("choose a port:"))
    #host = input("choose a host:")
    port = 5501
    host = "127.0.0.1"
    commande = input(f"Enter <CONNECT {host} {port}> to connect yourself:")
    if commande.upper() == f"CONNECT {host} {port}":
        nickname = input("choose a nickname:")
        client = Client(nickname,host,port)
        client.connect()
        receive_thread = threading.Thread(target=client.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=client.write)
        write_thread.start()
    
    else:
        print(f"Failed to connect")
    '''
    message = client.client.recv(1024).decode()

    if message == f'{client.nickname} is already taken':
        
        print("je sais pas encore") 
        client.nickname = input("choose another nickname:")'''