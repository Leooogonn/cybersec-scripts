#!/usr/bin/python3
import socket
import sys
import re

if len(sys.argv) != 4:
	print("Enumeracao de usuarios FTP")
	print("Modo de uso: python3 %s 127.0.0.1 2121 /usr/share/wordlists/names.txt"%(sys.argv[0]))
	sys.exit()

print("Interagindo com FTP Server")
ip = sys.argv[1]
porta = int(sys.argv[2])
wl = sys.argv[3]

# Iniciando laço de repetição
f = open(wl)
for user in f.readlines():
	print("Testando o usuario:",user)

# Realizando conexão
	msocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	msocket.connect((ip,porta))
	banner = msocket.recv(1024).decode('utf-8')

# Enviando dados
	query = "USER " + user + "\r\n"
	msocket.send(query.encode('utf-8'))
	resp = msocket.recv(1024).decode('utf-8')

	quit = "QUIT\r\n"
	msocket.send(quit.encode('utf-8'))
	banner = msocket.recv(1024).decode('utf-8')

# Tratando a resposta
	if re.search('331', resp):
		print("[+] Usuario encontrado:",user)


