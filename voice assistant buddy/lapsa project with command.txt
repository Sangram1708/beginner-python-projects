#import all modules
import speech_recognition as sr
import os
import subprocess
from datetime import *
import random
import pywhatkit
import pyjokes
import webbrowser
import wikipedia
import pyttsx3

#initialize the module
r = sr.Recognizer()
mic=sr.Microphone()

#initialize text to speech convertor
engine = pyttsx3.init()

#creating class for voice assistant
class lapsaproject:
    def __init__(self):
        self.r=sr.Recognizer()
        self.mic=sr.Microphone()
    # it will update all the things we have said to lapsa
    def user_history(self, command):
        today = str(date.today())
        today = today
        with open("history.txt", "a") as f:
              f.write( "On" + today + "User said : " + command + "\n")

    #to listen the command ,what user wants from lapsa
    def listen(self,mic, r):
        print("how can i help you,Waiting for command...")
        b.talk("how can i help you,Waiting for command...")
        try:
            with mic as source:
                # May reduce the time out in the future
                b.r.adjust_for_ambient_noise(source, duration=0.2)
                audio = b.r.listen(source)
                text = b.r.recognize_google(audio)
                text=text.lower()
                print(text)

                return text


        except sr.WaitTimeoutError:

            print("i have waited for your command ,plz start me again")

            b.talk("i have waited for your command ,plz start me again")
            pass

        except sr.UnknownValueError:

            print("you have given unknown name")

            b.talk("you have given unknown name")
            pass

        except sr.RequestError:

            print("Network error.")

            b.talk("Network error.")
            pass

    #it function is used to say the output from the command
    def talk(self,x):
        engine = pyttsx3.init()
        newVoiceRate = 120
        engine.setProperty('rate', newVoiceRate)
        engine.say(x)
        engine.runAndWait()
    #this function is used to close the app if it is opened
    def close_app(self,x):
        if "whatsapp" in x:
            os.system("TASKKILL /F /IM WhatsApp.exe")
        elif "firefox" in x:
            os.system("TASKKILL /F /IM firefox.exe")
        elif "notepad" in x:
            os.system("TASKKILL /F /IM notepad.exe")

    # this function is used to open the app
    def open_app(self,x):

        if x=="open whatsapp":
            subprocess.call("C://Users//Sangram//AppData//Local//WhatsApp//WhatsApp.exe")
        elif x=="open facebook":
            webbrowser.open("https://www.facebook.com")
        elif x=="open notepad":
            subprocess.call("Notepad.exe")
        elif x=="open photoshop":
            subprocess.call("C://Program Files//Adobe//Adobe Photoshop CS6 (x64)//Photoshop.exe")
        elif x=="open firefox":
            subprocess.call("C://Program Files (x86)//Mozilla Firefox//firefox.exe")


    #this function is used to play songs from youtube
    def playing(self,x):
        song = x.replace('play', '')
        b.talk('playing ' + song)
        pywhatkit.playonyt(song)

    #this function is used to clear the history
    def clear_history(self,x):
        file = open("history.txt", "r+")
        file.truncate(0)

    #it fuction will say about sangram
    def about_sangram(self,x):


        if "friends" in x:
            if "about" in x:
                print("Sangram's close friends are Ashok,Meenakshi Sundaram,Thomas,Subash,Guru")
                b.talk("Sangram's close friends are Ashok,Meenakshi Sundaram,Thomas,Subash,Guru")

        elif "education" in x:
            if "about" in x:
                print("studing B.E electronics and instrumentation engineering in Karpagam college in coimbatore and finished is 10th and 12th in Coimbatore")
                b.talk("studing BE electronics and instrumentation engineering in Karpagam college in coimbatore and finished is 10th and 12th in Coimbatore")

        elif "career" in x:
            if "about" in x:
                print("he has finished his 10th and 12th in coimbatore ,in 12th he got 636 and in 10th he got 363 ,in college upto 5th semester he got 7.97 and he is try for college placement")
                b.talk("he has finished his 10th and 12th in coimbatore ,in 12th he got 636 and in 10th he got 363 ,in college upto 5th semester he got 7.97 and he is try for college placement")

        elif "family" in x:
            if "about" in x:
                print("father : basant kumar nayak ,Mother : kabita nayak ,sir : muralitharannarayanan")
                b.talk("father : basant kumar nayak ,Mother : kabita nayak ,sir : muralitharannarayanan")

        elif "projects" or "project" in  x:
            if "about" in x:
                print("Home automation using remote control,and lapsa which is me ")
                b.talk("Home automation using remote control,and lapsa which is me ")
        elif "about" in x:
                print("Iam Sangram Nayak , Doing B.E engineering in karpagam college ,my age is 21 ,born on 17.8.2000 ,living in Coimbatore,Tamil Nadu ")
                b.talk("Iam Sangram Nayak , Doing BE engineering in karpagam college ,my age is 21 ,born on 17,08,2000 ,living in Coimbatore,Tamil Nadu ")


    #this function is used to search the word in browser
    def web_browse(self,x):
        b.talk("Here is what I found.")
        webbrowser.open("https://www.google.com/search?q={}".format(x))

    #this fuction is used to search for the which you are relating
    def start_command(self,x):
        try:

            if "sangram" in x:
                z = x.replace("laptop", "")
                b.about_sangram(z)
            elif "open" in x:
                z=x.replace("laptop","")
                b.open_app(z)
            elif command == "how are you":
                current_feelings = ["thankyou for asking ", "I'm doing well.what about you.", "I am doing okay ,what about your day"]
                # selects a random choice of greetings
                greeting = random.choice(current_feelings)
                b.talk(greeting)
            elif "clear history" in x:
                b.clear_history(x)

            #this loop is used for wikipedia summary
            elif 'wikipedia of' in x:
                try:
                    person = x.replace('wikipedia of','')
                    info =wikipedia.summary(person,3)
                    print(info)
                    b.talk(info)


                except:
                    print("i can't able to find it")
                    pass

            elif "close" in x:
                z = x.replace("laptop", "")
                b.close_app(z)
            elif "play" in x:
                z = x.replace("laptop", "")
                b.playing(z)
            #this loop is used for lapsa jokes
            elif "joke" in x:
                b.talk("this is the worst joke but it is much better than Ashok")
                c=pyjokes.get_joke("en")
                print(c)
                b.talk(c)

            elif "who" or "what" or "why" or "which" or "when" or "how" in x:
                z = x.replace("laptop", "")
                b.web_browse(z)


            else:
                b.talk("plz say the command again")
                pass
        except sr.WaitTimeoutError:
            print("i have waited for your command ,plz start me again")
            b.talk("i have waited for your command ,plz start me again")
            pass
        except sr.UnknownValueError:
            print("you have given unknown name")
            b.talk("you have given unknown name")
            pass
        except sr.RequestError:
            print("Network error.")
            b.talk("Network error.")
            pass




    #to wakeup Lapsa..
    def lapsa(self,mic,r):
        print("Say my name to start...")
        b.talk("Say my name to start...")
        try:
           with mic as source:
                b.r.adjust_for_ambient_noise(source, duration=0.2)
                audio = b.r.listen(source)
                text = b.r.recognize_google(audio)
                text=text.lower()
                print(text)
                if "john" in text:

                    return pas.text
                else:
                    pass
            #pass the error values
        except:
            pass


b=lapsaproject() #initializie the class
pas = b.lapsa(mic, r)
thankyou=True
n=0
while thankyou:
     command = b.listen(mic, r)
     if command:
         b.start_command(command)
         b.user_history(command)
     else:
         try:
             i=2
             if n==i:

                  print("thankyou for calling me i will be waiting for your command")
                  b.talk("thankyou for calling me i will be waiting for your command")
                  thankyou = False
             else :
                  n+=1
                  pass
         except:
             print("two chance remaining")
             pass