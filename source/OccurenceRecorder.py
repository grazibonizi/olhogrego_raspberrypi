# -- coding: utf-8 --
from VideoRecorder import VideoRecorder
from AudioRecorder import AudioRecorder
from ZipHelper import *
import threading
import time
import os
import shutil


class OccurenceRecorder(object):

    def __init__(self):
        self.folder_path = "../tmp"
        self.zip_file = "file.zip"
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
        zipdir(self.folder_path, self. zip_file)

    def clean_tmp_folder(self):
        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
