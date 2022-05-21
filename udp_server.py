import socket

IP = '0.0.0.0'
PORT = 9999

def main():
  server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  server.bind((IP, PORT))
  print(f'[*] Listening on {IP}:{PORT}')

  while True:
    data, addr = server.recvfrom(4096)
    print(data.decode())


if __name__ == '__main__':
  main()