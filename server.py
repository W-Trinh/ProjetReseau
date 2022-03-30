import socket
import threading


class Server:
    def __init__(self,address,port):
        self.address=address
        self.port=port
        self.clients=dict()
        self.commands=["QUIT","CHAT","ABS","BACK","LIST","EDIT","REFUSE","SEND","TELL","STOP","SFIC","ACCEPT","HELP"]
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def server_start(self):
        self.server.bind((self.address,self.port))
        self.server.listen()


    def broadcast(self,message):
        for client in self.clients:
            client.send(message)

    def handle(self,client):
        while True:
            try:
                message = client.recv(1024).decode("ascii")
                commande = message.split(" ")
                #print(client)
                if commande[0] == 'QUIT':
                    quitting_user = message.decode('ascii')
                    #quit_user(quitting_user)
                elif message.decode('ascii').startswith('LIST'):
                    #requesting_user = message.decode('ascii')
                    liste()
                elif message.decode('ascii').startswith('HELP'):
                    requesting_user = message.decode('ascii')
                    commands_list(requesting_user)
                elif commande[0] == 'EDIT':
                    verify_nickname(commande[1],client)
                elif message.decode('ascii').startswith('CHAT'):
                    self.broadcast(message)
                else:
                    self.broadcast(message)
            except:
                client.close()
                nickname = self.clients[client]
                self.broadcast(f'{nickname} left the chat !'.encode('ascii'))                                                                                        
                del self.clients[client]
                bre4ak


    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f'Connected with {str(address)}')
            client.send('nickname?'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            print(nickname)
            self.clients[client] = nickname
            print(f'Nickname of the client is {nickname} !')
            self.broadcast(f'{nickname} joined the chat! '.encode('ascii'))
            print(f'{nickname}')
            thread = threading.Thread(target=self.handle,args=(client,))
            thread.start()

    def verify_nickname(self,newNick,client):
        if newNick in self.clients.values():
            message=f'{newNick} is already taken'
            client.send(message)
        else:
            self.broadcast(f'{self.clients[client]} is now {newNick}'.encode('ascii'))
            self.clients[client]=newNick



    def quit_user(self,nom):
        pass



    def liste(self):
        pass
        #name_index = nicknames.index(nom)
        #requesting_client=clients[name_index]


    def commands_list(sock):
        while true:
            mess=sock.recv(1024)
            if mess.decode()=="":
                break
            sock.send(mess.upper())

print("server is listening ...")
serveur = Server('127.0.0.1',9133)
serveur.server_start()
serveur.receive()
serveur.nickname_existing()

