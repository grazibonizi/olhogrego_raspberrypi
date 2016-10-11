# -*- coding: utf-8 -*-
import time
from bluetooth import *


class BluetoothManager(object):

    def __init__(self):
        self.server_sock = BluetoothSocket(RFCOMM)
        self.server_sock.bind(("", PORT_ANY))
        self.server_sock.listen(1)
        self.port = self.server_sock.getsockname()[1]
        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
        advertise_service(self.server_sock, "TestServer",
        service_id=uuid,
        service_classes=[uuid, SERIAL_PORT_CLASS],
        profiles=[SERIAL_PORT_PROFILE])

    def run(self):
        print(("Waiting for connection on RFCOMM channel %d" % self.port))
        client_sock, client_info = self.server_sock.accept()
        print(("Connected to %r" % client_sock))
        while True:
            try:
                data = client_sock.recv(1024)
                if len(data) > 0:
                    print(("received [%s]" % data))
                    if data == 'Iniciar':
                        data = ('Iniciando gravacao as %s' % time.localtime())
                    elif data == 'Finalizar':
                        data = ('Iniciando gravacao as %s' % time.localtime())
                    else:
                        data = 'Comando nao reconhecido'
                    client_sock.send(data)
                    print(("sending [%s]" % data))

            except IOError:
                pass

            except KeyboardInterrupt:
                print("disconnected")
                client_sock.close()
                self.server_sock.close()
                print("all done")

                break
'''
        server_sock = BluetoothSocket(RFCOMM)
        server_sock.bind(("", PORT_ANY))
        server_sock.listen(1)
        port = server_sock.getsockname()[1]
        print(("listening on port %d" % port))
        uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
        advertise_service(server_sock, "BluetoothManager", uuid)
        while(True):
            client_sock, address = server_sock.accept()
            time.sleep(0.1)
            print(("Accepted connection from %s" % address))
            if len(address) > 0:
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

'''