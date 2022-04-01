import socket
import threading


class Server:
    def __init__(self,address,port):
        self.address=address
        self.port=port
        self.clients=dict()
        self.Connected=[]
        self.disconnected=[]
        self.commands=["QUIT","CHAT","ABS","BACK","LIST","EDIT","REFUSE","SEND","TELL","STOP","SFIC","ACCEPT","HELP"]
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def server_start(self):
        self.server.bind((self.address,self.port))
        self.server.listen()


    def broadcast(self,message):
        for client in self.clients:
            client.send(message.encode())

    def handle(self,client):
        boo = True
        while boo:
            try:
                message = client.recv(1024).decode("ascii")
                commande = message.split(" ",2)
                #print(client)
                if commande[1] == 'QUIT':
                    self.quit(client)
                elif commande[1] == 'LIST':
                    self.afficher_liste(client)

                elif commande[1] == 'HELP':
                    self.liste(client)
                elif commande[1] == 'EDIT':
                    self.verify_nickname(commande[2],client)
                elif commande[1] == 'CHAT':
                    msg = message.split(" ",1)
                    self.broadcast(self.clients[client] + " : " + commande[2])
                else:
                    client.send('the command was not found'.encode('ascii'))
            except:
                client.close()
                nickname = self.clients[client]
                self.broadcast(f'{nickname} left the chat !')                                                                                        
                del self.clients[client]
                break


    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f'Connected with {str(address)}')
            client.send('nickname?'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            self.clients[client] = nickname
            print(f'Nickname of the client is {nickname} !')
            self.broadcast(f'{nickname} joined the chat! ')
            self.Connected.append(nickname)
            thread = threading.Thread(target=self.handle,args=(client,))
            thread.start()

    def verify_nickname(self,newNick,client):
        if newNick in self.clients.values():
            message=f'{newNick} is already taken'
            client.send(message.encode())
        else:
            self.broadcast(f'{self.clients[client]} is now {newNick}')
            
            for i in range(len(self.Connected)):
                if self.Connected[i]==self.clients[client]:
                    self.Connected[i]=newNick
                else:
                    pass
            self.clients[client]=newNick
            
       
    def liste(self,client):
        #ex=print(*self.commands,sep=", ")
        s=" ,".join(self.commands)
        print(s)
        message=f'{s}'
        client.send(message.encode())


    def afficher_liste(self,client):
        s=" ,".join(self.Connected)
        print(s)
        message=f'{s}'
        client.send(message.encode())
        #s = " ,"
        #print(s.join(self.Connected))

    def quit(self,client):
        message="you have been disconnected"
        client.send(message.encode())
        self.Connected.remove(self.clients[client])
        name = self.clients[client]
        del self.clients[client]
        self.broadcast(f'{name} disconnected')
        #client.close()
        
            


    def commands_list(sock):
        while true:
            mess=sock.recv(1024)
            if mess.decode()=="":
                break
            sock.send(mess.upper())

print("server is listening ...")
serveur = Server('127.0.0.1',9261)
serveur.server_start()
serveur.receive()
serveur.nickname_existing()
