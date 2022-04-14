import socket
import threading


class Client():
    def __init__(self,nickname,address,port):
        self.nickname = nickname
        self.address = address
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.file_to_send = ""

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
                commande = message.split(":")
                print(commande)
                print(message)
                if message == "nickname?":
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    if commande[0].startswith("210"):
                        if "accepted the download" in commande[1].strip():
                            argument = commande[2].split(",")
                            self.send_file(argument[0].strip(), int(argument[1].strip()), self.file_to_send)
                        
                            
            except:
                print(message)
                print("an error has occured!")
                self.client.close()
                break

    def write(self):
        while True:
            message = input("")
            self.client.send(message.encode('ascii'))

            commande = message.split(" ")
            print(commande)

            if commande[0] == "ACCEPTFILE" and len(commande) == 5:
                self.accept_file(commande[4].strip(), int(commande[3].strip()), commande[2].strip())   

            if commande[0] == "SFIC" and len(commande) == 3:
                self.file_to_send = commande[2]
                
    def accept_file(self, addr, port, filename):
        print("Jaccepte un fichier")
        recvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        recvSocket.bind((addr, port))
        recvSocket.listen()
        while True:
            client, address = recvSocket.accept()
            f = open(filename, "wb")

            while True:
                data = client.recv(1024)
                f.write(data)
                if not data:
                    f.close()
                    break
            
            break
            
            f.close()
            client.close()
        recvSocket.close()       

    def send_file(self, addr, port, filename):
        print("jenvoi un fichier")
        print(addr)
        print(port)
        print(filename)
        sendSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sendSocket.connect( (addr,port) )

        f = open(filename, "rb")

        while True:
            data = f.read(1024)
            sendSocket.send(data)
            if not data:
                f.close()
                break

        sendSocket.close()

if __name__ == "__main__":
           
    nickname = input("choose a nickname:")
    port = int(input("choose a port:"))
    host = input("choose a host:")
    #port = 9900
    #host = "127.0.0.1"
    #commande = input(f"Enter CONNECT {host} {port} to connect yourself:")
    #if commande.upper() == f"CONNECT {host} {port}":

    client = Client(nickname,host,port)
    client.connect()
    receive_thread = threading.Thread(target=client.receive)
    receive_thread.start()

    write_thread = threading.Thread(target=client.write)
    write_thread.start()
    
#    else:
#        print(f"Failed to connect")
