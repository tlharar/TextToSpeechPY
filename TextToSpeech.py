from gtts import gTTS
from tkinter import *
import tkinter as tk
from playsound import playsound
from pydub import AudioSegment


def play():
    text = entry.get()
    speed = variable.get()
    lang = variable2.get()
    speed = speed.replace("x","")
    try:
        readText(text,lang.lower(),float(speed))
        
    except:
       print("write a text in text box.")
        

   

def readText(text,lang,speed):

    out = gTTS(text=text,lang=lang)
    out.save("read.mp3")
    audio = AudioSegment.from_mp3("read.mp3")
    speededAudio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed)
    })
    speededAudio= speededAudio.set_frame_rate(audio.frame_rate)
    speededAudio.export("reading.wav", format="wav")
    playsound("reading.wav")



master = Tk()
master.title('TextToSpeech')
master.geometry('750x200')
master.config(bg = '#000000')

variable = StringVar(master)
speeds = ["0.5x", "1.0x", "2.0"]
variable.set(speeds[1])

variable2 = StringVar(master)
langs = ["TR", "EN"]
variable2.set(langs[0])


optionMenu = OptionMenu(master, variable, *speeds)
optionMenu.config(width=40, bg = "#ff0000")
optionMenu.place(x=370,y = 60)

optionMenu2 = OptionMenu(master, variable2, *langs)
optionMenu2.config(width=40, bg = "#ff0000")
optionMenu2.place(x=20,y = 60)



entry = tk.Entry(font = "Verdana 14",width=59, bg = "#ff0000") 
entry.place(x=20,y=20)

buton = tk.Button(text="PLAY",command=play,width=40, bg = "#ff0000")
buton.place(x=200,y=110)




master.mainloop()