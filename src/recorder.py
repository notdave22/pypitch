import pyaudio
import os
import wave
import time

RECORDING = True
CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3

p = pyaudio.PyAudio()

chord_names = ['g_cmin_5','g_dmin_5','g_emin_5','g_fmin_5','g_gmin_5','g_amin_5','g_bmin_5']

n=0

while(RECORDING):
    inp = input("standby")

    if inp == 'r':
        time.sleep(3)
        print ("*recording*")
        #record audio for 3s
        frames = []
        #open stream
        stream = p.open(format=FORMAT,channels=CHANNELS,
                        rate=RATE,input=True,
                        frames_per_buffer=CHUNK
                        )
        for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print ("*done*")
        #close stream
        stream.stop_stream()
        stream.close()
        #ouput to file
        WAVE_OUTPUT_FILENAME = chord_names[n] + ".wav"
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        n = n+1
        
    if inp == 'q':
        print ("*exiting*")
        RECORDING = False
        
p.terminate()
