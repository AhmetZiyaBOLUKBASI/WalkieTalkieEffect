from pydub import AudioSegment
from pydub.generators import WhiteNoise

def add_radio_effect(input_file, output_file):
    # Load the input audio file
    sound = AudioSegment.from_wav(input_file)

    # High Pass Filter cut-off Frequency is 7500 kHz and 12 dB Amplifiyer

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

    # Export the modified audio to a new file
    radio_sound.export(output_file, format="wav")

if __name__ == "__main__":
    input_file = "input.wav"  # Specify the input .wav file
    output_file = "output_radio_effect.wav"  # Specify the output file with the radio effect
    add_radio_effect(input_file, output_file)
