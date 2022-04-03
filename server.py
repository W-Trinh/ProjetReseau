import socket
import threading


class Server:
    def __init__(self,address,port):
        self.address=address
        self.port=port
        self.clients=dict()
        self.away=[]
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
                    self.liste_clients(client)

                elif commande[1] == 'HELP':
                    self.liste_commandes(client)

                elif commande[1] == 'EDIT':
                    self.verify_nickname(commande[2],client)

                elif commande[1] == 'CHAT':
                    msg = message.split(" ",1)
                    self.broadcast(self.clients[client] + " : " + commande[2])

                elif commande[1] == 'SEND':
                    print(f'mon tableau: {commande} et sa taille: {len(commande)}')

                    if len(commande) < 3:
                        client.send("Missing parameter".encode())
                    elif commande[2] == " ":
                        client.send("Missing parameter".encode())
                    else:
                        self.send(client,commande[2])

                elif commande[1] == 'REFUSE':
                    print(f'mon tableau: {commande} et sa taille: {len(commande)}')
                    if len(commande) < 3:
                        client.send("Missing parameter".encode())
                    elif commande[2] == '':
                        client.send("Missing parameter".encode())
                    else:
                        self.refuse(client,commande[2])


                elif commande[1] == 'CONNECT':
                    pass

                elif commande[1] == 'ABS':
                    self.absent(client)

                elif commande[1] == 'BACK':
                    message="You are already online"
                    client.send(message.encode())
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
            self.etat=True              
        
            thread = threading.Thread(target=self.handle,args=(client,))
            thread.start()

    def absent(self,client):
        self.broadcast(f'{self.clients[client]} is now away')
        self.away.append(self.clients[client])
        while True:
            try:
                next_msg = client.recv(1024).decode("ascii")
                nxt = next_msg.split(" ",2)
                if nxt[1] == 'BACK':
                    self.broadcast(f'{self.clients[client]} is back')
                    break
                elif nxt[1] == "ABS":
                    message="You are already away"
                    client.send(message.encode())
                elif nxt[1] == "CHAT":
                    message="you can't send messages"
            except:
                print("an error")

        
    def send(self,client,receiver):
        if receiver in self.clients.values():
            if receiver == self.clients[client]:
                message = f"{self.clients[client]} is you, that means you can't have a private chat with yourself"
                client.send(message.encode())
            else:
                message = f"{self.clients[client]} wants to have a private a chat with you.respond with ACCEPT to accept the request or REFUSE to refuse"
                for key, valeur in self.clients.items(): 
                    if receiver == valeur: 
                        receiver_sock = key 

                receiver_sock.send(message.encode())

        else:
            print(f"408 {receiver} doesn't exist")
            message = f"408 {receiver} doesn't exist"
            client.send(message.encode())

        
    def refuse(self,client_to_respond,client_receiving_response):
        if client_receiving_response in self.clients.values():
            if client_receiving_response == self.clients[client_to_respond]:
                message = f"{self.clients[client_to_respond]} is you, that means you can't use this command to yourself"
                client_to_respond.send(message.encode())
            
            else:
                message = f"{self.clients[client_to_respond]} refused to have a private chat with you."
                for key, valeur in self.clients.items(): 
                    if client_receiving_response == valeur: 
                        client_receiving_response_sock = key 

                client_receiving_response_sock.send(message.encode())
        else:
            print(f"408 {client_receiving_response} doesn't exist")
            message = f"408 {client_receiving_response} doesn't exist"
            client_receiving_response.send(message.encode())

    def connect(self,client):
        pass


    def verify_nickname(self,newNick,client):
        if newNick in self.clients.values():
            message=f'{newNick} is already taken'
            client.send(message.encode())
        else:       
            self.broadcast(f'{self.clients[client]} is now {newNick}')
            for key in self.clients:
                if key == client:
                #if self.Connected[i]==self.clients[client]:
                    self.clients[client]=newNick
                    #print(f'verify:{self.clients}')


    def liste_commandes(self,client):
        #ex=print(*self.commands,sep=", ")
        s=" ,".join(self.commands)
        print(s)
        message=f'{s}'
        client.send(message.encode())


    def liste_clients(self,client):
        x = list(self.clients.values())
        x.sort()
        s=" ,".join(x)
        print(s)
        message=f'{s}'
        client.send(message.encode())


    def quit(self,client):
        message="you have been disconnected"
        client.send(message.encode())
        #self.Connected.remove(self.clients[client])
        name = self.clients[client]
        del self.clients[client]
        self.broadcast(f'{name} disconnected')
        self.client.close()
        

print("server is listening ...")
serveur = Server('127.0.0.1',9369)
serveur.server_start()
serveur.receive()
