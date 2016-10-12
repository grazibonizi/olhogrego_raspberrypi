# -*- coding: utf-8 -*-
import pyaudio
import wave
#import time


class AudioRecorder(object):

    def __init__(self):

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.p = pyaudio.PyAudio()
        path = '../tmp/'
        fileName = 'temp_audio'
        self.WAVE_OUTPUT_FILENAME = path + fileName + ".wav"
        self.frames = []
        self.keep_recording = 0
        self.stop_recording = 0

    def callback(self, in_data, frame_count, time_info, status):
        if (self.keep_recording == 1):
            self.frames.append(in_data)
        if(self.stop_recording == 0):
            return in_data, pyaudio.paContinue
        else:
            return in_data, pyaudio.paComplete

    def start(self):
        self.stream.start_stream()
        self.keep_recording = 1
        print("* recording audio")

    def prepare(self):
        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK,
                        stream_callback=self.callback)

    def stop(self):
        self.stop_recording = 1

    def cleanup(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print("* done recording audio")
