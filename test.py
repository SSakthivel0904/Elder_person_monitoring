import threading
import time
from difflib import SequenceMatcher
from tkinter import Tk, Canvas, NW, Entry
from tkinter import *

import pyttsx3
import speech_recognition as sr
from PIL import ImageTk

import ar_master
mm= ar_master.master_flask_code()

class sample:
    def __init__(self):
        self.master='ar_master'
        self.title ='Elder Person Monitoring'
        self.titlec ='ELDER PERSON MONITORING'
        self.backround_color ='##2F4F4F	'
        self.text_color ='#c0c0c0'
        self.backround_image='images/background_hd1.jpg'
    def get_title(self):
        return self.title
    def get_titlec(self):
        return self.titlec
    def get_backround_color(self):
        return self.backround_color
    def get_text_color(self):
        return self.text_color
    def get_backround_image(self):
        return self.backround_image



    def chat_window(self):


        chat_app_root = Tk()
        get_data = sample()
        w = 780
        h = 500
        ws = chat_app_root.winfo_screenwidth()
        hs = chat_app_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        chat_app_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        chat_app_root.title(get_data.get_title())
        chat_app_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        canvas = Canvas(chat_app_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
                           fill=get_data.get_text_color())
        admin_id1 = canvas.create_text(390, 70, text="CHAT", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(100, 120, text="USER : ", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(200, 120, text="arun", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())

        admin_id2 = canvas.create_text(100, 170, text="TYPE : ", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(200, 170, text="sad", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())

        status_id = canvas.create_text(400, 120, text="Loading...", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        global e1
        global w1, e2
        e1 = Entry(canvas, font=('times', 15, ' bold '))

        canvas.create_window(400, 170, window=e1)
        w1 = StringVar()

        e2 = Label(canvas, font=('times', 15, ' bold '), width=40,height=10, textvariable=w1,anchor="nw")
        canvas.create_window(450, 320, window=e2)
        def SpeakText(command):
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()
        def SpeakText1(command):
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()
            voice_input()
        def change_text():
            canvas.itemconfig(status_id, text='Recognizing...')
        def change_text1():
            canvas.itemconfig(status_id, text='Loading...')
        def voice_input():
            text=''
            try:
                chat_app_root.after(500, change_text)
                e1.delete(0, END)
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio_data = r.record(source, duration=4)
                    text = r.recognize_google(audio_data)
                    previous_data=w1.get()
                    w1.set(previous_data+"\nUser : "+str(text))
            except:
                print("**")
            qq = "select * from query_details where status='Sad'"
            print(qq)
            data1 = mm.select_direct_query(qq)
            max=0
            result='ask me again'
            for row in data1:
                perc=SequenceMatcher(None, text, row[1]).ratio()
                if perc>max:
                    result=row[2]
                    max=perc
            SpeakText1(result)
        def exit_program():
            change_text()
            voice_input()
            time.sleep(500)
            change_text1()

        b1 = Button(canvas, text="Start", command=exit_program, font=('times', 15, ' bold '))
        canvas.create_window(600, 120, window=b1)
        def test():
            user="Welcome "
            first_text="Why your feeling sad"
            w1.set(user)
            SpeakText(user)
            SpeakText(first_text)
            canvas.update_idletasks()
        chat_app_root.after_idle(test)
        # chat_app_root.after_idle(threading.Thread(target=test).start())
        chat_app_root.mainloop()



# s=sample()
# s.chat_window()
#
