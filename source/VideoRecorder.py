# -- coding: utf-8 --
import pygame
import pygame.camera
from pygame.locals import *
import time
import threading


class VideoRecorder(object):
    def __init__(self):
        # this is where one sets how long the script
        # sleeps for, between frames.sleeptime__in_seconds = 0.05
        # initialise the display window
        self.screen = pygame.display.set_mode([800, 420])
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
                # blank out the screen
                self.screen.fill([0, 0, 0])
                # copy the camera image to the screen
                self.screen.blit(image, (100, 0))
                # update the screen to show the latest screen image
                pygame.display.update()
                #save picture
                instante = str(int(round(time.time() * 1000)))
                imgAtual = '../tmp/' + instante + '.jpg'
                pygame.image.save(image, imgAtual)
                # sleep between every frame
                time.sleep(0.16)
                if self.stop_recording == 1:
                    break
            except KeyboardInterrupt:
                break
        print("* done recording video")

    def stop(self):
        self.stop_recording = 1
        time.sleep(0.5)
        self.cam.stop()
        pygame.quit()

    def start(self):
        video_thread = threading.Thread(target=self.record)
        self.cam.start()
        return video_thread