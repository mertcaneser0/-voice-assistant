from email.mime import audio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

r = sr.Recognizer()


def record( ask = False) :
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            print("Lana:Ne söylediğini anlayamadım")
        except sr.RequestError:
            print("Lana:Çalışamıyorum")
        return voice 







def speak(string) :
    tts = gTTS(text=string,lang='tr')
    file="answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("Merhaba mert")
voice=record()
if voice != '' :
    print(voice)

    if "ne haber " in voice :
        speak("Sana nasıl yardımcı olabilirim")


    