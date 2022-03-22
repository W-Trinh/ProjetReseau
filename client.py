import socket,sys
import threading


if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <adresse> <port>",file=sys.stderr)
    sys.exit(1)

with socket.socket() as sock_locale:
    sock_locale.connect((sys.argv[1], int(sys.argv[2])))
    print (f"Connexion vers ' à l'adresse {sys.argv[1]} et au port {str(sys.argv[2])} + ' reussie.")
    while True:
        commande = input("Entrez une commande (quit pour quitter) : ")
        if commande.upper() == "QUIT":
            break
        sock_locale.send(commande.encode())
        reponse = sock_locale.recv(256)
        print(reponse.decode())



