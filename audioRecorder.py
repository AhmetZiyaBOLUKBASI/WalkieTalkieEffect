# Some of the below python codes copied from pyaudio official documentation. 
# https://people.csail.mit.edu/hubert/pyaudio/#record-example

import wave
import sys

import pyaudio

import keyboard 

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100

with wave.open('output.wav', 'wb') as wf:
    p = pyaudio.PyAudio()
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

    isStartting = input("Start Recording by hitting 't':")
    
    if isStartting == "t":

        print("To Stop Recording Press 't' !")

        while True:
            wf.writeframes(stream.read(CHUNK))
            if keyboard.is_pressed("t"):
                break

    stream.close()
    p.terminate()