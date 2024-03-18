import wave
import sys

import pyaudio

import keyboard

from pydub import AudioSegment
from pydub.generators import WhiteNoise

from datetime import datetime

class WalkieTalkie():


    def __init__(self,outFileName):

        # Initialization function. In the function user records voice like
        # "<filename-2024xxxx.wav" file. After the records ends, add_radio_effect
        # function calls and original record editing.

        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1 if sys.platform == 'darwin' else 2
        RATE = 44100

        now = datetime.now()
        dateStr = now.strftime("%Y%m%d%H%M%S")
        originalRecord = outFileName + '-' + dateStr + '.wav'

        with wave.open(originalRecord, 'wb') as wf:
            p = pyaudio.PyAudio()
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)

            stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

            print ("To Start Recording Please Press 'Space' !")

            event = keyboard.read_event()

            if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
                
                # We wait for cleaning keyboard buffer below while loop.
                while keyboard.is_pressed("space") :
                    pass

                print("To Stop Recording Please Press 'Space' !")
                print("Recording ...")

                while True:
                    wf.writeframes(stream.read(CHUNK))
                    if keyboard.is_pressed("space"):
                        break

                print("Recording has finished")

            stream.close()
            p.terminate()

        self.__originalRecord = originalRecord

        self.add_radio_effect()

    def add_radio_effect(self):
        # This function first applied 7,5 kHz High-Pass Filter, then amplified
        # 12 dB, and finally added white noise after this process beep sound was added 
        # at the beginning and the end of the speech. 

        # Load the input audio file
        sound = AudioSegment.from_wav(self.__originalRecord)

        # High Pass Filter cut-off Frequency is 7500 Hz and 12 dB Amplifiyer

        sound_highpass = sound.high_pass_filter(7500) + 12

        beep_sound = AudioSegment.from_wav("beep.wav")

        # Create white noise for the radio effect
        noise = WhiteNoise().to_audio_segment(duration=len(sound_highpass), volume=sound_highpass.dBFS)

        # Add noise to the audio
        radio_sound = sound_highpass.overlay(noise)

        # Lower the pitch of the audio to make it sound like an old radio
        radio_sound = radio_sound._spawn(radio_sound.raw_data, overrides={
            "frame_rate": int(radio_sound.frame_rate * 0.99)  # Decrease frame rate to lower pitch
        })

        radio_sound = beep_sound + radio_sound + beep_sound

        outEffectFile = self.__originalRecord.split("-")[0] + "-radio-" + self.__originalRecord.split("-")[1]

        # Export the modified audio to a new file
        radio_sound.export(outEffectFile, format="wav")

        self.__radioEffectRecord = outEffectFile

    def playRecord(self,recordType) :
        # In this function, we play our records. If we call <object name>playRecord("original")
        # ıt plays our first record. If we call <object name>playRecord("radio").

        CHUNK = 1024

        if recordType == "original" :

            recordFile = self.__originalRecord
        
        elif recordType == "radio" :

            recordFile = self.__radioEffectRecord

        else : 

            print("""Wrong Keyword!\nUsage\n\t<Object Name>.playRecord(original | radio)\n
                  Please Use one of 'original' or 'radio' keywords!""")
            sys.exit(-1)

        with wave.open(recordFile, 'rb') as wf:

            # Instantiate PyAudio and initialize PortAudio system resources (1)
            p = pyaudio.PyAudio()

            # Open stream (2)
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            # Play samples from the wave file (3)
            while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                stream.write(data)

            # Close stream (4)
            stream.close()

            # Release PortAudio system resources (5)
            p.terminate()