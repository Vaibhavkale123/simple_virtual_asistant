import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from send2trash import send2trash
import automate_browser


def browsing(text):
    automate_browser.search(text)
    #os.system('python automate_browser.py')



def speak(text):
    tts = gTTS(text=text,lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    send2trash(filename)
    

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said =""

        try:
            said = r.recognize_google(audio)
            print (said)
        except Exception as e:
            print("Exception:"+str(e)+ "say something clearly")

    return said

# text=get_audio()
# browsing(text)
while True:
    text = get_audio()
    if "hello" in text:
        speak("Hello,Vaibhav")
    elif "browsing" in text:
        speak("Say. What you want to search")
        text=get_audio()
        browsing(text)
    elif "stop" or "break" in text:
       speak("Do you want to Stop?")
       text=get_audio()
       if "yes" in text:
           break
       else:
            pass



     #   speak("we will go in game")
      #  path = "D:\Games"
       # path = os.path.realpath(path)
        #print(path)
        #os.startfile(path)

##if"time" in text:
##    speak(f"{time}")
###if = open("experimen.txt","w")
###if.write(text)
###if.close()
