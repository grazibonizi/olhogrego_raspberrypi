# -- coding: utf-8 --
from VideoRecorder import VideoRecorder
from AudioRecorder import AudioRecorder
import threading
import time
import os
import shutil


class OccurenceRecorder(object):

    def __init__(self):
        self.clean_tmp_folder()
        self.audioRecorder = AudioRecorder()
        self.videoRecorder = VideoRecorder()

    def start_recording(self):
        self.audioRecorder.prepare()
        self.videoRecorder.prepare()
        #waits initialization
        time.sleep(1)
        self.videoRecorder.start()
        self.audioRecorder.start()

    def stop_recording(self):
        self.audioRecorder.stop()
        self.videoRecorder.stop()
        while threading.active_count() > 1:
            time.sleep(0.1)
        self.audioRecorder.cleanup()
        self.videoRecorder.cleanup()

    def clean_tmp_folder(self):
        folder = "../tmp"
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)