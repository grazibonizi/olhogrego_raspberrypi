# -- coding: utf-8 --
import pygame
import pygame.camera
from pygame.locals import *
import time
import threading


class VideoRecorder(object):
    def __init__(self):
        pygame.init()
        pygame.camera.init()
        # set up a camera object
        self.cam = pygame.camera.Camera("/dev/video0", (640, 480))
        self.stop_recording = 0

    def record(self):
        print("* recording video")
        while 1:
            try:
                 # fetch the camera image
                image = self.cam.get_image()
                #save picture
                instante = str(int(round(time.time() * 1000)))
                imgAtual = '../tmp/' + instante + '.jpg'
                pygame.image.save(image, imgAtual)
                # sleep between every frame
                time.sleep(0.5)
                if self.stop_recording == 1:
                    break
            except KeyboardInterrupt:
                break
        print("* done recording video")

    def stop(self):
        self.stop_recording = 1

    def prepare(self):
        self.cam.start()

    def start(self):
        video_thread = threading.Thread(target=self.record)
        video_thread.start()

    def cleanup(self):
        self.cam.stop()
        pygame.quit()