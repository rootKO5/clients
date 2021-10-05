import socket 

target_port = "www.google.com"
target_port = 80

# create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((hostname, port))

client.sendall('hola amigos\n');

data = '' 
while (data != '/exit'):
  try:
    data = raw_input('>> ')
    if (data != '/exit'):
      response = client.recv(4096);
      print(response);
  except EOFError:
    break
