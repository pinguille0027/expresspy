import yaml
import socket

with open('config.yml', 'r') as file:
  config = yaml.safe_load(file)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((config['address'], config['port']))
  s.listen()
  while True:
    clientsocket, address = s.accept()
    print(f"hola desde {address}")
    clientsocket.send(bytes("puta", "utf-8"))
    