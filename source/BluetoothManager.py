# -*- coding: utf-8 -*-
import time
from bluetooth import *
from OccurenceRecorder import OccurenceRecorder


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
        print(("Connected to %r" % client_sock))
        while True:
            try:
                data = client_sock.recv(1024)
                if len(data) > 0:
                    print(("received [%s]" % data))
                    if data == 'Iniciar':
                        data = ('Iniciando gravacao as %s' % time.localtime())
                        self.occurenceRecorder.start_recording()
                    elif data == 'Finalizar':
                        data = ('Finalizando gravacao as %s' % time.localtime())
                        self.occurenceRecorder.stop_recording()
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
