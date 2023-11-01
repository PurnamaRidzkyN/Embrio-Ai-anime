import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import subprocess
import requests
import webbrowser
import os 
import datetime
from googlesearch import search
import requests
from PyQt5.QtWidgets import QApplication, QPushButton



folder_path = r"C:\purna\program\myai\nahida\sound nahida"

# Inisialisasi dictionary untuk menyimpan file audio
audio_files = {}

# Iterasi melalui seluruh file dalam folder
for filename in os.listdir(folder_path):
    if filename.endswith(".wav"):
        file_path = os.path.join(folder_path, filename)
        audio = AudioSegment.from_wav(file_path)
        audio_files[filename] = audio

response_menyerah = audio_files.get("jika aku menyerah.wav")
response_cape = audio_files.get("why.wav")
response_kenapa = audio_files.get("alasan.wav")
response_lelah = audio_files.get("lelah.wav")
awal = audio_files.get("awal.wav")
suaraTidakTerdengar = audio_files.get("tidak terdengar.wav")
game = "C:\Program Files\Genshin Impact\launcher.exe"
url = "https://anoboy.today/"

recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000
timeout_duration = 3
button = False
play(awal)

while not button:
    print("Tekan 'S' untuk bicara, 'Q' untuk keluar.")
    choice = input().lower()

    if choice == 's' :
        if not button:
            print("Silakan bicara...")
            with sr.Microphone() as source:
                try:
                    audio = recognizer.listen(source, timeout=timeout_duration)
                    text = recognizer.recognize_google(audio, language="id-ID")
                    print("Anda berkata:", text)

                    if "nyerah" in text.lower():
                        play(response_menyerah)
                        button = False
                    elif "cape" in text.lower():
                        play(response_cape)
                        button= False
                    elif "kenapa" in text.lower():
                        play(response_kenapa)
                        button = False
                    elif "game" in text.lower():
                        subprocess.Popen([game])
                        button = True
                    elif "anime" in text.lower():
                        webbrowser.open(url)
                        button = True
                    elif "lelah" in text.lower():
                        play(response_lelah)
                        button = False
                    
                except sr.WaitTimeoutError:
                    print("Waktu bicara habis. Silakan tekan 'S' lagi untuk bicara.")
                except sr.UnknownValueError:
                    play(suaraTidakTerdengar)
                    print("Maaf suara tidak kedengeran")
                except sr.RequestError:
                    print("Maaf, terjadi kesalahan pada layanan pengenalan suara.")
        else:
            print("Semoga harimu menyenangkan")
            button = True

    elif choice == 'q':
        break