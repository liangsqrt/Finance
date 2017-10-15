import socket


socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket1.connect(('127.0.0.1',20010))
socket1.send('get_proxy')
data=socket1.recv(1024)
print data