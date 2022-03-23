import socket,sys,threading
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <port>", file=sys.stderr)
    sys.exit(1)


sock_locale= socket.socket()
sock_locale.bind(("", int(sys.argv[1])))
sock_locale.listen(4)
taille_tampon = 256

def traiter_client(sock_fille):
    while True:
        mess = sock_fille.recv(256)
        if mess.decode() == "":
            break
        sock_fille.sendall(mess.upper())

while True:
    try:
        sock_client, adr_client = sock_locale.accept()
        requete = sock_client.recv(256)

        #requete = sock_locale.recvfrom(256)
        commande, adr_client) = requete
        ip_client,port_client = adr_client

        com = commande.decode().lower()
        message = "200 Requête incorrect : " + commande.decode()
      
        if com == "help":
            message = " a lot a lot exemple :)"
        sock_locale.sendto(message.encode(),adr_client)
        
        #threading.Thread(target=traiter_client, args=(sock_client,)).start()
    

    except KeyboardInterrupt:
        break

sock_locale.shutdown(socket.SHUT_RDWR)
print("Bye")
for t in threading.enumerate():
    if t != threading.main_thread(): t.join


sys.exit(0)