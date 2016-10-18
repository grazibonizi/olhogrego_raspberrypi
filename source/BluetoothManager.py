# -*- coding: utf-8 -*-
#import time
from bluetooth import *
from OccurenceRecorder import OccurenceRecorder
#from lightblue import *


class BluetoothManager(object):

    def __init__(self):
        self.server_sock = BluetoothSocket(RFCOMM)
        self.server_sock.bind(("", PORT_ANY))
        self.server_sock.listen(1)
        self.port = self.server_sock.getsockname()[1]
        self.occurenceRecorder = OccurenceRecorder()
        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
        advertise_service(self.server_sock, "TestServer",
        service_id=uuid,
        service_classes=[uuid, SERIAL_PORT_CLASS],
        profiles=[SERIAL_PORT_PROFILE])

    def run(self):
        print(("Waiting for connection on RFCOMM channel %d" % self.port))
        client_sock, client_info = self.server_sock.accept()
        print(("Connected to %s" % client_info[0]))
        while True:
            try:
                data = client_sock.recv(1024)
                if len(data) > 0:
                    print(("received [%s]" % data))
                    if data == 'Iniciar':
                        print('Iniciando gravacao')
                        self.occurenceRecorder.start_recording()
                    elif data == 'Finalizar':
                        self.occurenceRecorder.stop_recording()
                        data = self.readfile("file.zip")
                        client_sock.send(data)
                        print('Arquivo enviado')
                    else:
                        print('Comando nao reconhecido')

            except IOError:
                pass

            except KeyboardInterrupt:
                print("disconnected")
                client_sock.close()
                self.server_sock.close()
                print("all done")

                break

    #def getservice(self, target_address):
        #services = lightblue.findservices(target_address)
        #for service in services:
            #if service[2] == "OBEX Object Push":
                #obex_port = service[1]
            #break
        #return obex_port

    def readfile(self, filename):
        in_file = open(filename, "rb")
        in_bytes = in_file.read()
        in_file.close()
        return in_bytes