import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import subprocess
import requests
import webbrowser
import os 

folder_path = r"C:\purna\program\myai\kafka\sound kafka"

audiofiles={}
for filename in os.listdir(folder_path):
  if filename.endswith(".wav"):
      file_path=os.path.join(folder_path,filename)
      audio = AudioSegment.from_wav(file_path)
      audiofiles[filename]=audio

opening = audiofiles.get("opening.wav")
respon_cape = audiofiles.get("cape.wav")
respon_mau = audiofiles.get("mau.wav")

recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000
timeout_duration = 3
button = False
play(opening)

while not button:
   print("tekan (s) untuk belajar, tekan (q) untuk keluar ")
   choice = input().lower()

   if choice == 's':
      if not button:
         print("silahkan berbicara....")
         with sr.Microphone() as source :
            try:
               audio = recognizer.listen(source,timeout=timeout_duration)
               text = recognizer.recognize_google(audio,language="id-ID")
               print("anda berkata : ", text)

               if "cape" in text.lower():
                  play(respon_cape)
                  print("tekan (s) untuk belajar, tekan (q) untuk keluar ")
                  choice = input().lower()

                  if choice == 's':
                     if not button:
                        print("silahkan berbicara....")
                        with sr.Microphone() as source :
                           
                              audio = recognizer.listen(source,timeout=timeout_duration)
                              text = recognizer.recognize_google(audio,language="id-ID")
                              print("anda berkata : ", text)
                              if "mau" in text.lower():
                                 play(respon_mau)
                                 continue
               
            except sr.WaitTimeoutError:
               print("kelamaan lo")
            except sr.UnknownValueError:
               print("maaf gak kedengaran")
               play()
            except sr.RequestError:
               print("maaf lag")
      else:
         print("nanti datang lagi ya")
         button=True
   elif choice == "q":
      break
   
