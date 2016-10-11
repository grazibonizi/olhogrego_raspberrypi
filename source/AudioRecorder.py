import pyaudio
import wave
import threading
import time


class AudioRecorder(object):

    def __init__(self):

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        #nome do arquivo de audio
        path = '../tmp/'
        fileName = 'temp_audio'
        self.WAVE_OUTPUT_FILENAME = path + fileName + ".wav"
        self.frames = []
        self.stop_recording = 0

    def record(self):
        print("* recording audio")
        while 1:
            try:
                data = self.stream.read(self.CHUNK)
                self.frames.append(data)
                if self.stop_recording == 1:
                    break
            except KeyboardInterrupt:
                break
        print("* done recording audio")

    def stop(self):
        self.stop_recording = 1
        time.sleep(0.5)
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def start(self):
        audio_thread = threading.Thread(target=self.record)
        return audio_thread