import pyaudio
import wave
import time


class audioRecorder:
    def __init__(self,
                 filename='recorded_audio.wav',
                 channels=1,
                 sample_rate=44100,
                 duration=5,
                 chunk=1024,
                 format=pyaudio.paInt16):
        self.filename = filename
        self.channels = channels
        self.sample_rate = sample_rate
        self.duration = duration
        self.chunk = chunk
        self.format = format
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def start_recording(self):
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.sample_rate,
                                      input=True,
                                      frames_per_buffer=self.chunk)

    def stop_recording(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()

    def save_to_file(self):
        frames = []
        start_time = time.time()
        while time.time() - start_time < self.duration:
            data = self.stream.read(self.chunk)
            frames.append(data)
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()
