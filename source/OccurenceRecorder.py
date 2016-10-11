# -- coding: utf-8 --
from VideoRecorder import VideoRecorder
#from AudioRecorder import AudioRecorder
import threading
import time
import os
import shutil


class OccurenceRecorder(object):

    def __init__(self):
        #self.audioRecorder = AudioRecorder()
        self.videoRecorder = VideoRecorder()
        self.filename = "gravacao"
        self.clean_tmp_folder()

    def start_recording(self):
        #audio_thread = self.audioRecorder.start()
        video_thread = self.videoRecorder.start()
        #aguarda inicializacao da camera
        time.sleep(0.5)
        #audio_thread.start()
        video_thread.start()

    def stop_recording(self):
        #self.audioRecorder.stop()
        self.videoRecorder.stop()
        while threading.active_count() > 1:
            time.sleep(0.5)

    def clean_tmp_folder(self):
        folder = "../tmp"
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)