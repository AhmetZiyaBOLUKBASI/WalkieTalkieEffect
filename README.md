# Voice Recorder with Walkie Talkie Radio Effect in Python

## Summary

This project was created for fun :upside_down_face:. Basically, when you use the project, you will get two .wav record one of original record and one of added radio sound effect to your record. If you want to get a sample .wav file edited by the project, please [click here](https://drive.google.com/u/0/uc?id=1GN2oRKm2N_wLv7fQsQ6QhonHdwBCOJVC&export=download). For more details about usage keep reading !.

## Contributors And Contact Info

*   Ahmet Ziya BÖLÜKBAŞI - a_z_bolukbasi@outlook.com

## Usage

### Prequirisity

* _Python 3_
* _pyaudio_
* _pydub_
* _keyboard_

### Installation and Execution

> [!WARNING]   
> Please be sure you have prequirisities that 
> expressed in the previous section in your environment. 

Clonning project repo:

`git clone https://github.com/AhmetZiyaBOLUKBASI/WalkieTalkieEffect.git`

Access  the folder you have cloned and execute your python interpreter :

```
cd WalkieTalkieEffect
python3
```

Import walkieTalkieTool.py and create an object with WalkieTalkie() class:

```
from walkieTalkieTool import WalkieTalkie as wt
myObject = wt("output")
```

Now, you will see in terminal `To Start Recording Please Press 'Space' !`. Press space to start recording when you ready.

To finish recording please press space again. After stopping the record you have two sound files: "_output-2024aaaaaaa.wav_" and "_output-radio-2024aaaaaaa.wav_" in the project folder. "_output-2024aaaaaaa.wav_" is your original record, and "_output-radio-2024aaaaaaa.wav_" is your record with walkie-talkie effect. To listen to your original record run `myObject.playRecord("original")`.To listen to your record with walkie-talkie effect run `myObject.playRecord("radio")`.

## License

There is no license for fun :sunglasses:. You can use the project free but your stars and feedbacks will make me happy. Have fun.