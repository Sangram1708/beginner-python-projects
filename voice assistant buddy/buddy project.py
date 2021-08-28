#import all modules
import speech_recognition as sr
import os
import sys
from pygame import mixer
import subprocess
from datetime import *
import time
from glob import glob
import random
from playsound import playsound
import pywhatkit
import pyjokes
import webbrowser
import wikipedia
import pyttsx3


#creating class for voice assistant
class Buddyproject:
    def __init__(self):
        self.r=sr.Recognizer()
        self.mic=sr.Microphone()
    def all_history(self, command):
        today = str(date.today())
        now=datetime.now()
        currenttime=now.strftime("%H:%M:%S %A")
        today = today
        with open("allhistory.txt", "a") as f:
              f.write( "On" ","+ today + ", " + currenttime +", " "User said : " + command + "\n")    
    # it will update all the things we have said to lapsa
    def user_history(self, command):
        today = str(date.today())
        now=datetime.now()
        currenttime=now.strftime("%H:%M:%S %A")
        today = today
        with open("history.txt", "a") as f:
              f.write( "On" + today + " " + currenttime +" " "User said : " + command + "\n")

    #to listen the command ,what user wants from lapsa
    def listen(self,mic, r):
        try:
            print("Waiting for command...")
            
            with self.mic as source:
                b.talk("Waiting for command...")
                # May reduce the time out in the future
                b.r.energy_threshold = 300
                audio = b.r.listen(source)
                text = b.r.recognize_google(audio)
                text=text.lower()


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
        elif "wps" in x:
            os.system("TASKKILL /F /IM ksolaunch.exe")     

    # this function is used to open the app
    def open_app(self,x):

        if "whatsapp" in x:
            subprocess.call("C://Users//Sangram//AppData//Local//WhatsApp//WhatsApp.exe")
        elif "facebook" in x:
            webbrowser.open("https://www.facebook.com")
        elif "notepad" in x:
            subprocess.call("Notepad.exe")
        elif "photoshop" in x:
            subprocess.call("C://Program Files//Adobe//Adobe Photoshop CS6 (x64)//Photoshop.exe")
        elif "youtube" in x:
            webbrowser.open("https://www.youtube.com")

        elif "wps office" in x:
            subprocess.call("C://Users//Sangram//AppData//Local//Kingsoft//WPS Office//ksolaunch.exe")     


    #this function is used to play songs from youtube
    def playing(self,x):
        try:
            if "video" in x:
                if "play" in x:
                    song = x.replace('play', '')
                    b.talk('playing ' + song)
                    pywhatkit.playonyt(song)
            elif "music" in x:
                if "play" in x:
                    if "motivational" in x:
                        if "tamil" in x:
                            mixer.init()
                            print("playing motivational song in Tamil ....")
                            path="C://Users//Sangram//Desktop//music//tamilmotivational//"
                            listen=os.listdir(path)
                            c=random.choice(listen)
                            mixer.music.load(f"C://Users//Sangram//Desktop//music//tamilmotivational//{c}") # Music file can only be MP3
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.perf_counter()
                            
                        elif "english" in x:
                            print("playing motivational song in English ....")
                            mixer.init()
                            path="C://Users//Sangram//Desktop//music//englishmotivational"
                            listen=os.listdir(path)
                            c=random.choice(listen)
                            mixer.music.load(f"C://Users//Sangram//Desktop//music//englishmotivational//{c}") # Music file can only be MP3
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.perf_counter()
                            
                    
                    elif "romantic" in x:
                        if "tamil" in x:
                            print("playing Romatic song in Tamil ....")
                            mixer.init()
                            path="C://Users//Sangram//Desktop//music//tamilromatic"
                            listen=os.listdir(path)
                            c=random.choice(listen)
                            mixer.music.load(f"C://Users//Sangram//Desktop//music//tamilromatic//{c}") # Music file can only be MP3
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.perf_counter()
                                
                        elif "english" in x:
                            print("playing Romatic song in English ....")
                            mixer.init()
                            path="C://Users//Sangram//Desktop//music//englishromatic"
                            listen=os.listdir(path)
                            c=random.choice(listen)
                            mixer.music.load(f"C://Users//Sangram//Desktop//music//englishromatic//{c}") # Music file can only be MP3
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.perf_counter()
        except:
        
            pass


    #this function is used to clear the history
    def clear_history(self,x):
        file = open("history.txt", "r+")
        file.truncate(0)

    #it fuction will say about sangram
    def about_sangram(self,x):
        if "who is" in x:
            print("Sangram Nayak , Doing B.E engineering in karpagam college  , his age is 21 ,born on 17.8.2000 ,living in Coimbatore,Tamil Nadu ")
            b.talk("Sangram Nayak , Doing BE engineering in karpagam college ,his age is 21 ,born on 17 8 2000 ,living in Coimbatore,Tamil Nadu ")        

        elif "friends" in x:
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
                print("Home automation using remote control,and Buddy which is me ")
                b.talk("Home automation using remote control,and Buddy which is me ")        

        
        
        


    #this function is used to search the word in browser
    def web_browse(self,x):
        b.talk("Here is what I found.")
        z=webbrowser.open("https://www.google.com/search?q={}".format(x))
        

    #this fuction is used to search for the which you are relating
    def start_command(self,x):
        try:

            if 'sangram' in x:
                z = x.replace("buddy", "")
                b.about_sangram(z)
            elif "open" in x:
                z=x.replace("buddy","")
                b.open_app(z)
            elif 'how are you'  in x:
                current_feelings = ["thankyou for asking ", "I'm doing well.what about you.", "I am doing okay ,what about your day"]
                # selects a random choice of greetings
                greeting = random.choice(current_feelings)
                b.talk(greeting)

            elif "clear" in x:
                if "history" in x:
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
                z = x.replace("buddy", "")
                b.close_app(z)
            elif "play" in x:
                z = x.replace("buddy", "")
                b.playing(z)
                

            #this loop is used for lapsa jokes
            elif "joke" in x:
                b.talk("this is the worst joke but it is much better than Ashok")
                c=pyjokes.get_joke("en")
                print(c)
                b.talk(c)
            

            elif "say something" in x:
                if "about you" in x:
                    print("iam a voice assistant like siri which is created by Sangram Nayak ") 
                    b.talk("iam a voice assistant like siri which is created by Sangram Nayak ")   

            elif "who" or "what" or "why" or "which" or "when" or "how" in x:
                z = x.replace("buddy", "")
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

#initialize the module
r = sr.Recognizer()
mic=sr.Microphone()

#initialize text to speech convertor
engine = pyttsx3.init()



b=Buddyproject() #initializie the class
while True:
               try:
                    with mic as source:
                         print("Buddy is always waiting for your command")
                         b.r.energy_threshold = 300
                         audio = b.r.listen(source)
                         text = b.r.recognize_google(audio)
                         text=text.lower()
                         print(text)
                         if "buddy" in text:
                              print("how can i help you")
                              b.talk("how can i help you")
                              thankyou=True
                              n=0
                              while thankyou:
                                   command = b.listen(mic, r)
                                   if command:
                                        if "thank you" in command:
                                             print("thankyou for calling me i will be waiting for your command")
                                             b.talk("thankyou for calling me i will be waiting for your command")
                                             thankyou=False
                                             break
                                             
                                             
                                        else:  
                                             b.start_command(command)
                                             b.user_history(command)  
                                             b.all_history(command)
                                             time.sleep(10)
                                             
                                        
                                   else:
                                        try:
                                             i=2
                                             if n==i:

                                                  print("thankyou for calling me i will be waiting for your command")
                                                  b.talk("thankyou for calling me i will be waiting for your command")
                                                  thankyou = False
                                             else :
                                                  print("{} chance is remaining ".format(i-n))
                                                  n+=1
                                                  pass
                                        except:
                                             pass
                                                  
                         else:
                              pass

               except:
                     pass