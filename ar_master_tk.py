import time
from tkinter import Tk, messagebox, ttk
from tkinter import *
from tkinter.messagebox import askyesno
import imagehash
import cv2
from PIL import Image, ImageTk
import numpy as np
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.models import Sequential
import os
from keras.preprocessing.image import ImageDataGenerator
import pyttsx3
import speech_recognition as sr
from PIL import ImageTk
import ar_master
mm= ar_master.master_flask_code()
from test import sample
from difflib import SequenceMatcher
mm = ar_master.master_flask_code()
train_dir = 'data/train'
val_dir = 'data/test'
num_train = 28709
num_val = 7178
batch_size = 64
num_epoch = 50
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(48,48),
        batch_size=batch_size,
        color_mode="grayscale",
        class_mode='categorical')
validation_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=(48,48),
        batch_size=batch_size,
        color_mode="grayscale",
        class_mode='categorical')
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
chat_emotions=["Sad","Angry","Disgusted"]
class tk_master:
    care_taker=''
    user=''
    emotion=''
    def __init__(self):
        self.master='ar_master'
        self.title ='Elder Person Monitoring'
        self.titlec ='ELDER PERSON MONITORING'
        self.backround_color ='#2F4F4F	'
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
    def chat_app(self):
        print(tk_master.user,tk_master.emotion)
        chat_app_root =Toplevel()
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
        admin_user = canvas.create_text(200, 120, text="-", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())

        admin_id2 = canvas.create_text(100, 170, text="TYPE : ", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        admin_type = canvas.create_text(200, 170, text="-", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())

        status_id = canvas.create_text(400, 120, text="Loading...", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        global e1,tree
        global w1, e2
        e1 = Entry(canvas, font=('times', 15, ' bold '))

        canvas.create_window(400, 170, window=e1)
        w1 = StringVar()


        e2 = Label(canvas, font=('times', 10, ' bold '), width=50, height=15, textvariable=w1, anchor="w")

        canvas.create_window(450, 320, window=e2)


        def SpeakText(command):
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()
            engine.stop()


        def SpeakText1(command):
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()
            engine.stop()

            # voice_input()


        def voice_input():
            canvas.update()
            canvas.itemconfig(status_id, text='Loading...')
            text = ''
            if 1==1:
                e1.delete(0, END)
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio_data = r.record(source, duration=4)
                    text = r.recognize_google(audio_data)
                    previous_data = w1.get()
                    w1.set(previous_data + "\nUser : " + str(text))
                    print(test)
                    canvas.update()
                    time.sleep(1)

            canvas.itemconfig(status_id, text='Recognizing...')
            qq = "select * from query_details where status='Sad'"
            data1 = mm.select_direct_query(qq)
            max = 0.5
            result = 'ask me again'
            for row in data1:
                perc = SequenceMatcher(None, text, str(row[1]).lower()).ratio()
                if perc > max:
                    result = str(row[2]).lower()
                    max = perc
            SpeakText1(result)
            previous_data = w1.get()
            w1.set(previous_data + "\nBot : " + str(result))
            canvas.update()
            time.sleep(1)
            voice_input()
        def exit_program():
            voice_input()
        b1 = Button(canvas, text="Start", command=exit_program, font=('times', 15, ' bold '))
        canvas.create_window(600, 120, window=b1)

        def test():
            get_data = tk_master()
            user = "Hellow "+get_data.user
            first_text = "Why your feeling "+get_data.emotion
            w1.set(user)
            # SpeakText(user)
            # SpeakText(first_text)
            canvas.itemconfig(admin_user, text=get_data.user)
            canvas.itemconfig(admin_type, text=get_data.emotion)
            canvas.itemconfig(status_id, text='Loading...')
            canvas.update_idletasks()
            engine = pyttsx3.init()
            engine.say(user)
            engine.runAndWait()
            engine.stop()

        chat_app_root.after_idle(test)
        chat_app_root.mainloop()

    def video_on(self):
        def image_matching(a, b):
            i1 = Image.open(a)
            i2 = Image.open(b)
            assert i1.mode == i2.mode, "Different kinds of images."
            assert i1.size == i2.size, "Different sizes."
            pairs = zip(i1.getdata(), i2.getdata())
            if len(i1.getbands()) == 1:
                dif = sum(abs(p1 - p2) for p1, p2 in pairs)
            else:
                dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
            ncomponents = i1.size[0] * i1.size[1] * 3
            xx = (dif / 255.0 * 100) / ncomponents
            return xx
        def match_templates(in_image):
            name = []
            values = []
            entries = os.listdir('train/')
            for x in entries:
                val = 100
                name.append(x)
                x1 = "train/" + x
                arr = os.listdir(x1)
                for x2 in arr:
                    path = x1 + "/" + str(x2)
                    find = image_matching(path, in_image)
                    hash0 = imagehash.average_hash(Image.open(path))
                    hash1 = imagehash.average_hash(Image.open(in_image))
                    cc1 = hash0 - hash1
                    find = cc1
                    if (find < val):
                        val = find
                values.append(val)
            values_lenght = len(values)
            pos = 0;
            pos_val = 100
            for x in range(0, values_lenght):
                if values[x] < pos_val:
                    pos = x
                    pos_val = values[x]
            # print(pos_val)
            if (pos_val < 27):
                print(pos, pos_val, name[pos])
                return name[pos]
            else:
                return "No"
        model.load_weights('model.h5')
        i=0
        dir = r'frame'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        if not os.path.exists(dir):
            os.makedirs(dir)
        video_capture = cv2.VideoCapture(0)
        data=True
        while data:
            ret, frame = video_capture.read()
            str1=os.path.join(dir , str(i)+'.jpg')
            lastimg = cv2.resize(frame, (100, 100))
            cv2.imwrite(str1, lastimg)
            i+=1
            ######################
            facecasc = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                prediction = model.predict(cropped_img)
                maxindex = int(np.argmax(prediction))
                result=(emotion_dict[maxindex])
                msg='No'
                ar = match_templates(str1).strip()
                msg=ar+":"+result
                print(msg)

                if result in chat_emotions and ar != 'No':
                    answer = askyesno(title='Result',message=str(msg))
                    if answer and len(ar)>0:
                        data = False
                        tk_master.user=ar
                        tk_master.emotion=result
                        break
                        time.sleep(1)
                    time.sleep(1)
                cv2.putText(frame, (msg), (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow('Emotion', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif data != True:
                break
        video_capture.release()
        cv2.destroyWindow('Emotion')
        if data != True:
            tk_master.user = ar
            tk_master.emotion = result
            print(tk_master.user,tk_master.emotion)
            tt = tk_master()
            tt.chat_app()

    def face_register_login(self):
        dir = r'frame'
        if not os.path.exists(dir):
            os.makedirs(dir)
        face_register_root = Toplevel()
        get_data = tk_master()
        w = 780
        h = 500
        ws = face_register_root.winfo_screenwidth()
        hs = face_register_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        face_register_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        face_register_root.title(get_data.get_title())
        face_register_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas2 = Canvas(face_register_root, width=200, height=300)
        canvas2.pack(fill="both", expand=True)

        canvas2.create_image(0, 0, image=bg, anchor=NW)
        # canvas.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas2.create_text(390, 20, text="FACE REGISTER", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        vlabl_id=canvas2.create_text(250, 120,text="Username", font=("Times New Roman", 20),fill=get_data.get_text_color())
        e1 = Entry(canvas2, font=('times', 15, ' bold '))
        canvas2.create_window(250, 190, window=e1)

        image = Image.open('images/face.png')
        img = image.resize((150, 150))
        my_img = ImageTk.PhotoImage(img)

        image_id1 = canvas2.create_image(500, 200, image=my_img)
        def exit_program():
            user = e1.get()
            if (user == ""):
                messagebox.showinfo(title="Alert", message="Enter Name", parent=face_register_root)
            else:
                cascPath = "data/haarcascades/haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(cascPath)
                train = True
                video_capture = cv2.VideoCapture(0)
                name = "train"
                if os.path.exists(name):
                    h = 0
                else:
                    os.mkdir(name)
                name1 = "train\\" + user
                if os.path.exists(name1):
                    j = 0
                else:
                    os.mkdir(name1)
                k = 0
                i = 0
                while True:
                    # Capture frame-by-frame
                    ret, frame = video_capture.read()

                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    ######
                    if (frame is None):
                        print("Can't open image file")
                    face_cascade = cv2.CascadeClassifier(cascPath)
                    faces = face_cascade.detectMultiScale(frame, 1.1, 3, minSize=(100, 100))
                    if (faces is None):
                        print('Failed to detect face')
                    if (True):
                        for (x, y, w, h) in faces:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                    facecnt = len(faces)
                    height, width = frame.shape[:2]
                    for (x, y, w, h) in faces:
                        r = max(w, h) / 2
                        centerx = x + w / 2
                        centery = y + h / 2
                        nx = int(centerx - r)
                        ny = int(centery - r)
                        nr = int(r * 2)

                        faceimg = frame[ny:ny + nr, nx:nx + nr]
                        lastimg = cv2.resize(faceimg, (100, 100))

                        k += 1
                        # print(k)
                        if ((k < 20) & (k >= 5)):
                            str1 = name1 + '\\%d.jpg' % k
                            cv2.imwrite(str1, lastimg)
                            i += 1
                            print(i)
                    if i >= 15:
                        # image1=os.path.join("images/background_hd1.jpg")
                        # image1=os.path.join("train\\"+user,"10.jpg")
                        # image = Image.open(image1)
                        # img = image.resize((250, 250))
                        # my_img = ImageTk.PhotoImage(img)
                        # global image_id1

                        # canvas2.itemconfig(image_id1, image=my_img)
                        # global image_id2
                        # image_id1.itemconfig(image=my_img)
                        #
                        # image_id2.config(image=my_img)
                        break
                    cv2.imshow('Video', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                video_capture.release()
                # cv2.waitKey(5000)
                cv2.destroyWindow('Video')
                # canvas.itemconfig(image_id1, image=my_img)
                # cv2.destroyWindow("Video")
                # load_image()
                # name1 = "train\\" + user+"\\15.jpg"
        b1 = Button(canvas2, text="Register", command=exit_program, font=('times', 15, ' bold '))
        b1.pack()
        canvas2.create_window(250, 300, window=b1)

        face_register_root.mainloop()

    def care_taker_home(self):
        care_taker_home_root = Toplevel()
        get_data = tk_master()
        w = 780
        h = 500
        ws = care_taker_home_root.winfo_screenwidth()
        hs = care_taker_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        care_taker_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        care_taker_home_root.title(self.title)
        care_taker_home_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(care_taker_home_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(390, 20, text=self.title, font=("Times New Roman", 24), fill=self.text_color)
        admin_id2 = canvas.create_text(390, 70, text="CARE TAKER HOME", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        ###
        def clickHandler(event):
            tt = tk_master
            # tt.face_register_login(event)
            tt.face_register_login(event)

        image = Image.open('images/face.png')
        img = image.resize((150, 150))
        my_img = ImageTk.PhotoImage(img)
        image_id = canvas.create_image(250, 170, image=my_img)
        canvas.tag_bind(image_id, "<1>", clickHandler)

        ###
        def clickHandler1(event):
            tt = tk_master
            tt.video_on(event)
            # tt.chat_app(event)

        image1 = Image.open('images/video.png')
        img1 = image1.resize((150, 150))
        my_img1 = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(250, 370, image=my_img1)
        canvas.tag_bind(image_id1, "<1>", clickHandler1)
        ###
        admin_id = canvas.create_text(420, 170, text="Face Register", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", clickHandler)
        ###
        admin_id1 = canvas.create_text(420, 370, text="Video ON", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id1, "<1>", clickHandler1)
        care_taker_home_root.mainloop()
    def care_taker_registration(self):
        care_taker_registration_root = Toplevel()
        care_taker_registration_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = care_taker_registration_root.winfo_screenwidth()
        hs = care_taker_registration_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        care_taker_registration_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        care_taker_registration_root.resizable(False, False)
        canvas1 = Canvas(care_taker_registration_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
        #                     fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 20, text="CARE TAKER REGISTRATION", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 70, text="Name", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 120, text="Contact", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 170, text="Email", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 220, text="Address", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 270, text="Username", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 320, text="Password", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())

        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 70, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 120, window=e2)
        e3 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 170, window=e3)
        e4 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 220, window=e4)
        e5 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 270, window=e5)
        e6 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 320, window=e6)

        def exit_program():
            name = e1.get()
            contact = e2.get()
            email = e3.get()
            address = e4.get()
            username = e5.get()
            password = e6.get()
            if (name == ""):
                messagebox.showinfo(title="Alert", message="Enter Name", parent=care_taker_registration_root)
            elif (contact == ""):
                messagebox.showinfo(title="Alert", message="Enter Contact", parent=care_taker_registration_root)
            elif (email == ""):
                messagebox.showinfo(title="Alert", message="Enter Email", parent=care_taker_registration_root)
            elif (address == ""):
                messagebox.showinfo(title="Alert", message="Enter Address", parent=care_taker_registration_root)
            elif (username == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=care_taker_registration_root)
            elif (password == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=care_taker_registration_root)
            else:
                maxin = mm.find_max_id("care_taker_details")
                qry = ("insert into care_taker_details values('" + str(maxin) + "','" + str(name) + "','" + str(
                    contact) + "','" + str(email) + "','" + str(address) + "','" + str(username) + "','" + str(
                    password) + "','0','0')")
                result = mm.insert_query(qry)
                messagebox.showinfo(title="Alert", message="Registration Success", parent=care_taker_registration_root)
                care_taker_registration_root.destroy()
        b1 = Button(canvas1, text="Register", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        care_taker_registration_root.mainloop()
    def care_taker_login(self):
        care_taker_login_root =Toplevel()
        care_taker_login_root.attributes('-topmost', 'true')
        get_data=tk_master()
        w = 780
        h = 500
        ws = care_taker_login_root.winfo_screenwidth()
        hs = care_taker_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        care_taker_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        care_taker_login_root.resizable(False, False)
        canvas1 = Canvas(care_taker_login_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24), fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="CARE TAKER LOGIN", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 200, text="Username", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 300, text="Password", font=("Times New Roman", 24), fill=get_data.get_text_color())
        def clickHandler1(event):
            tt = tk_master()
            tt.care_taker_registration()
        new_register_id = canvas1.create_text(440, 450, text="New Registration Here...", font=("Times New Roman", 24),fill=get_data.get_text_color())
        canvas1.tag_bind(new_register_id, "<1>", clickHandler1)
        e1 = Entry(canvas1,font=('times', 15, ' bold '))
        canvas1.create_window(470, 200, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '),show="*")
        canvas1.create_window(470, 300, window=e2)
        def exit_program():
            a=e1.get()
            b=e2.get()
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=care_taker_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=care_taker_login_root)
            else:
                qry = "SELECT * from care_taker_details where username='" +str(a)+ "' and password='"+ str(b)+ "'"
                result = mm.select_login(qry)
                if result == "no":
                    messagebox.showinfo("Result","Login Failed", parent=care_taker_login_root)
                else:
                    tt = tk_master()
                    tt.care_taker=str(a)
                    messagebox.showinfo("Result","Login Success", parent=care_taker_login_root)
                    care_taker_login_root.destroy()

                    tt.care_taker_home()
        b1=Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        care_taker_login_root.mainloop()
    def admin_login(self):
        admin_login_root =Toplevel()
        admin_login_root.attributes('-topmost', 'true')
        get_data=tk_master()
        w = 780
        h = 500
        ws = admin_login_root.winfo_screenwidth()
        hs = admin_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        admin_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        admin_login_root.resizable(False, False)
        canvas1 = Canvas(admin_login_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24), fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="ADMIN LOGIN", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 200, text="Username", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 300, text="Password", font=("Times New Roman", 24), fill=get_data.get_text_color())
        e1 = Entry(canvas1,font=('times', 15, ' bold '))
        canvas1.create_window(470, 200, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '),show="*")
        canvas1.create_window(470, 300, window=e2)
        def exit_program():
            a=e1.get()
            b=e2.get()
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=admin_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=admin_login_root)
            elif((a=="sakthi")and(b=="cora")):
                messagebox.showinfo("Result","Login Success", parent=admin_login_root)
                admin_login_root.destroy()
                tt = tk_master()
                tt.admin_home()
            else:
                messagebox.showinfo("Result","Login Failed", parent=admin_login_root)
        b1=Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        admin_login_root.mainloop()
    def admin_home(self):
        admin_home_root = Toplevel()
        admin_home_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = admin_home_root.winfo_screenwidth()
        hs = admin_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        admin_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        admin_home_root.resizable(False, False)
        canvas1 = Canvas(admin_home_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="ADMIN TRAIN DATA", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 200, text="Emotion", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 300, text="Query", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 400, text="Response", font=("Times New Roman", 24),fill=get_data.get_text_color())
        variable = StringVar(canvas1)
        variable.set("Sad")  # default value

        w = OptionMenu(canvas1, variable, "Sad", "Angry","Disgusted")
        canvas1.create_window(470, 200, window=w)

        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(470, 300, window=e1)

        e2 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=e2)
        def exit_program():
            a = e1.get()
            b = e2.get()
            type=variable.get()
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Query", parent=admin_home_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Response", parent=admin_home_root)
            else:
                maxin = mm.find_max_id("query_details")
                qry = ("insert into query_details values('" + str(maxin) + "','" + str(a) + "','" + str( b) + "','"+str(type)+"','0')")
                result = mm.insert_query(qry)
                messagebox.showinfo(title="Alert", message="Success", parent=admin_home_root)
                admin_home_root.destroy()
                tt = tk_master()
                tt.admin_home()
        b1 = Button(canvas1, text="Train Data", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 450, window=b1)
        admin_home_root.mainloop()
    def set_window_design(self):
        root = Tk()
        w = 780
        h = 500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        root.title(self.title)
        root.resizable(False,False)
        bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(390, 20, text=self.title, font=("Times New Roman", 24), fill=self.text_color)
        ###
        def clickHandler(event):
            tt=tk_master
            tt.admin_login(event)
        image = Image.open('images/admin.png')
        img = image.resize((150, 150))
        my_img = ImageTk.PhotoImage(img)
        image_id=canvas.create_image(250, 170,  image=my_img)
        canvas.tag_bind(image_id, "<1>", clickHandler)
        ###
        def clickHandler1(event):
            tt = tk_master
            tt.care_taker_login(event)
        image1 = Image.open('images/studentss.png')
        img1 = image1.resize((150, 150))
        my_img1 = ImageTk.PhotoImage(img1)
        image_id1=canvas.create_image(250, 370,  image=my_img1)
        canvas.tag_bind(image_id1, "<1>", clickHandler1)
        ###
        admin_id=canvas.create_text(420, 170, text="Admin", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", clickHandler)
        ###
        admin_id1 = canvas.create_text(420, 370, text="Care Taker", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id1, "<1>", clickHandler1)
        root.mainloop()
ar=tk_master()
root=ar.set_window_design()

