# -*- coding: utf-8 -*-
import time
from bluetooth import *

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY))
server_sock.listen(1)
port = server_sock.getsockname()[1]
print(("listening on port %d" % port))
uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
client_sock, address = ()


def wait_for_connections():
    advertise_service(server_sock, "FooBar Service", uuid)
    while(True):
        client_sock, address = server_sock.accept()
        time.sleep(0.1)
        print(("Accepted connection from %s" % address))
        if len(address) > 0:
            run()
            break


def run():
    while(True):
        try:
            data = client_sock.recv(1024)
            if len(data) > 0:
                print(("received [%s]" % data))
                if(data == 'Iniciar'):
                    print('o dispositivo iniciara a gravacao agora')
        except IOError:
            pass
        except KeyboardInterrupt:
            print("disconnected")
            client_sock.close()
            server_sock.close()
            print("all done")

            break