#!/usr/bin/python3

## Script que realiza o mesmo processo do utilitário whois em python.

import socket,sys

if len(sys.argv) <= 1:
        print ("Modo de uso: python3 whois.py [DOMAIN]")
        print ("Exemplo: python3 whois.py amazon.com.br")
else:
        query = sys.argv[1] + "\r\n"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect (("whois.iana.org",43))
        s.send(query.encode('latin-1'))
        resposta = s.recv(1024).split()
        whois = resposta[19]

        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.connect((whois,43))
        s1.send(query.encode('latin-1'))
        resp = s1.recv(8096).decode('latin-1')
        print(resp)
