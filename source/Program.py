# -- coding: utf-8 --
from VideoRecorder import VideoRecorder
from AudioRecorder import AudioRecorder
import threading
import time
import os
import shutil


class Program(object):

    def __init__(self):
        self.audioRecorder = AudioRecorder()
        self.videoRecorder = VideoRecorder()
        self.filename = "gravacao"

    def start_recording(self):
        audio_thread = self.audioRecorder.start()
        video_thread = self.videoRecorder.start()
        #aguarda inicializacao da camera
        time.sleep(0.5)
        audio_thread.start()
        video_thread.start()

    def stop_recording(self):
        self.audioRecorder.stop()
        self.videoRecorder.stop()
        while threading.active_count() > 1:
            time.sleep(0.5)
        #frame_counts = video_thread.frame_counts
        #elapsed_time = time.time() - video_thread.start_time
        #recorded_fps = frame_counts / elapsed_time
        #print "total frames " + str(frame_counts)
        #print "elapsed time " + str(elapsed_time)
        #print "recorded fps " + str(recorded_fps)
        #video_thread.stop()

        # Makes sure the threads have finished
        #while threading.active_count() > 1:
        #    time.sleep(1)
        # Merging audio and video signal
        #if abs(recorded_fps - 6) >= 0.01:# If the fps rate was higher/
        ##lower than expected, re-encode it to the expected
            #print "Re-encoding"
            #cmd = "ffmpeg -r " + str(recorded_fps)
            #+ " -i temp_video.avi -pix_fmt yuv420p -r 6 temp_video2.avi"
            #subprocess.call(cmd, shell=True)
            #print "Muxing"
            #cmd = "ffmpeg -ac 2 -channel_layout stereo -i temp_audio.wav "
            #+ "-i temp_video2.avi -pix_fmt yuv420p " + filename + ".avi"
            #subprocess.call(cmd, shell=True)
        #else:
            #print "Normal recording\nMuxing"
            #cmd = "ffmpeg -ac 2 -channel_layout stereo -i temp_audio.wav "
            #+ "-i temp_video.avi -pix_fmt yuv420p " + filename + ".avi"
            #subprocess.call(cmd, shell=True)
            #print ".."

    # Required and wanted processing of final files
    def clean_tmp_folder(self):
        folder = "../tmp"
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

if __name__ == '__main__':
    program = Program()
    program.clean_tmp_folder()
    program.start_recording()
    time.sleep(10)
    program.stop_recording()
    print ("Processo finalizado.")