import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import wikipedia 
from requests import get
import webbrowser
import pywhatkit
import sys
import time
import pyjokes
import pyautogui
import requests
import smtplib
# import instadownloader
# import instaloader
import PyPDF2
# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import QTimer, QTime, QDate, Qt
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
# from.jarvisgui import ui_jarvisgUi

# ui_jarvisgUi()

# from PyQt5.uic import loadUiType
# from PyQt5.QtWidgets import QApplication, QMainWindow

# # Load the UI file dynamically
# Ui_MainWindow, QMainWindowBase = loadUiType("jarvisgui")

# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())













engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# take command  to convert voice into text
def takecommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("listening...")
       r.pause_threshold = 1
       audio = r.listen(source,timeout=5,phrase_time_limit=5)

   try:
       print("Recognizing...")
       query = r.recognize_google(audio, language='en-in')
       print(f"user said: {query}")

   except Exception as e :
       speak("Unable To Catch,Please Say That Again...")
       return "none"
   
   return query 

# to make jarvis wish/greet 
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>= 0 and hour<=12:
        speak("good morning Harsh Dodiwan")
        speak("I am jarvis sir. Please tell me how can i help you")
        
    elif hour>=12 and hour<=18:
        speak("good afternoon sejal singh ")
      #   speak("I am jarvis sejal mam . Please tell me beautiful lady how can i help you")
      #   speak("hi sejal ")
        
    else:
        speak("good evening harsh dodiwan")
        speak("I am jarvis sir. Please tell me how can i help you")

# &&&&&&&&&&&&&&&&&&&  to send email ***********


def sendEmail(to , content):
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshdodiwan@gmail.com', 'ch@nge975@')
    server.sendEmail('harshdodiwan@gmail.com', to , content)
    server.close()

   ############## to read pdf ######################

def pdf_reader():
   book = open('harsh kumar final project.pdf', 'rb')
   pdfReader = PyPDF2.pdfFileReader(book)
   pages = pdfReader.numPages
   speak(f"total number of pages in this book{pages}")
   speak("sir please enter the page number i have to read")
   pg = int(input("please enter the page number:"))
   page = pdfReader.getPage(pg)
   text = page.extractText()
   speak(text)
   
def news():
   main_url = '6b6cb5cf89264a8696ec2edc5aa1801f'

   main_page = requests.get(main_url).json()
   print(main_page)
   articles = main_page["articles"]
   print(articles)
   head = {}

   day =["first", "second", "third", "fourth", "fifth" , "sixth" , "seventh" , "eighth" , "ninth", "tenth" ]
   for ar in articles:
      head.append(ar["title"])
   for i in range (len(day)):
      print(f"today's {day[i]} news is:" , head[i])
      speak(f"today's {day[i]} news is:" , head[i])
 
if __name__ == "__main__":
    # speak("this is harsh dodiwan jarvis")
    # takecommand()
    wish()


    while True:
    # while true open notepad till the function not completed executed


    # if 1 use to open notepad only one time 
    # if 1: 
    # Assuming this is for some condition check, like always-true for testing

     query = takecommand().lower()

    # Logic building for tasks

     if "open notepad" in query:
        apath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2408.12.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
        os.startfile(apath)  # This needs to be indented inside the 'if' block

     elif "open command prompt" in query:
        os.system("start cmd")  # Proper indentation for the 'elif' block
     
     elif "closed notepad" in query:
         speak = ("okay sir , closing notepad")
         os.system("taskkill/f/im Notepad.exe")

     elif "open brave" in query:
        npath = "C:\\Users\\harsh\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        os.startfile(npath)  # This needs to be indented inside the 'if' block

     elif "open instagram" in query:
        ipath = "https://www.instagram.com/"
        os.startfile(ipath)  # This needs to be indented inside the 'if' block


     elif "open spotify" in query:
        spath = "C:\\Users\\harsh>\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
        os.startfile(spath)  # This needs to be indented inside the 'if' block


    # elif "open camera" in query:
    #     cpath = "https://www.instagram.com/"
    #     os.startfile(cpath)  # This needs to be indented inside the 'if' block



    # ******************* # now we play music **************

     elif "play music" in query:
        music_dir = "C:\\Users\\harsh\\OneDrive\\Desktop\\music"
        songs = os.listdir(music_dir)
        # os.startfile(os.path.join(music_dir,songs[0]))

        # to play random songs 
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir,rd))



    #  ******************   # to know ip addess of the system *******


     elif "ip address" in query:
        ip = get('https://api.ipify.org').text
        speak(f"your ip address is {ip}")

        

     elif "wikipedia" in query:
        speak("searching wikipedia...")
        query = query.replace("wikipedia", " ")
        results = wikipedia.summary(query , sentences = 3)
        speak("According to wikipedia")
        speak(results)
        print(results)

    # elif "open youtube" in query:
    #     webbrowser.open("youtube.com")

     elif "open youtube" in query:
        speak("sir, what should i search on youtube")
        cm = takecommand().lower()
        webbrowser.open(f"{cm}")

     elif "open linkedin" in query:
        webbrowser.open("linkedin.com")

     elif "open instagram" in query:
        webbrowser.open("instagram.com")

     elif "open github" in query:
        webbrowser.open("github.com")

    # elif "open google" in query:
    #     webbrowser.open("google.com")

     elif "open google" in query:
        speak("sir, what should i search on google")
        cm = takecommand().lower()
        webbrowser.open(f"{cm}")

     elif "send message" in query:
        pywhatkit.sendwhatmsg("+919958230825", "this is testing protocol" , 00,35)


     elif "play song on youtube" in query:
        pywhatkit.playonyt("tujhe main pyaar karu")



     elif "email to harsh" in query:
      try:
         speak("what should i say?")
         content = takecommand().lower()
         to = "harshdodiwan@gmail.com"
         sendEmail(to , content)
         speak("email has been sent to harsh dodiwan")

      except Exception as e:
            print(e)
            speak("sorry i cant send the email to your desirable person")

     elif "no thanks" in query:
        speak("thankyou for using me sir, have a good day")
        sys.exit()


        # to set a alarm
     elif "set alarm" in query:
        nn=int(datetime.datetime.now().hour)
        if nn == 1:
            music_dir="C:\\Users\\harsh\\OneDrive\\Desktop\\music"
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

     elif "tell me a joke" in query:
        joke = pyjokes.get_joke()
        speak(joke)

     elif "shut down the system" in query:
        os.system("shutdown /s /t 5")
 
     elif "restart the system" in query:
        os.system("shutdown /s /t 5")
    
     elif "sleep the system" in query:
        os.system("rund1132.exe powerprof.dll,SetSusoendState 0,1,0")

     elif "switch the window" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")

     elif "tell me the news" in query:
         speak("please wait sir, fetching the latest news")
         news()




         ###########   to find location ##############

     elif "where i am" in query or "where we are" in query:
      speak("wait sir ,let me check")
      try:

        ip = get('https://api.ipify.org').text
        speak(f"your ip address is {ip}")
        url = 'https://get.geojs.io/v1/ip/geo/' +ip+'.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json
        city = geo_data['city']
        country = geo_data['country']
        speak( f"sir,we are in {city} city of the {country} country") 

      except Exception as e :
         speak("sorry sir , due to network issue i an not able to find where we are")
                          

         ##############  to download instagram picture ###############


   #   elif "instagram profile" in query or "profile on instagam" in query:
   #    speak("sir please enter the user name correctly")
   #    name = input("harsh_dodiwan :")
   #    webbrowser.open(f"www.instagram.com/{name}")
   #    speak("sir , here is the profile of the user{name}")
   #    time.sleep(5)
   #    speak("sir, ould you like to download the profile picture of this accont")
   #    condition = takecommand().lower()
   #    if "yes" in condition:
   #       mod = instaloader.instaloader()
   #       mod.download_profile("harsh_dodiwan",profile_pic_only = True)
   #       speak("i am done sir , profile picture is saved in our main folder")
   #   else:
   #       pass
                   



          ##############  take a screenshot ###############


     elif "take screenshot" in query or "take a screenshot" in query:
         speak("str,please tell me the name for this screenshot file")
         name = takecommand().lower()
         speak("please , sir hold the screen for few seconds, i am taking screenshot ")
         time.sleep(3)
         img = pyautogui.screenshot()
         img.save(f"{name}.png")
         speak("i am done sir , the screenshot is savex in our main folder.now i an take a screenshot")


      
           ##################   to read pdf file  ##############


     elif "read pdf" in query :
         pdf_reader()


         #####################  to hide files and folder ##############


     elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
        speak("sir please tell me you want to hide this folder or make it visible for everyone")
        condition = takecommand().lower()
        if "hide" in condition:
           os.system("attrib +h /s /d")
           speak("sir , all the files in this folder are now hidden.")

        elif "visible" in condition:
           os.system("attrib -h /s /d")
           speak("sir, all the files in this folder are now visible to everyone.")
           

        elif "leave it " in condition:
           speak("ok sir.")

     speak("sir, do you have any other work")

    
  #######################  #############  code after making gui #############################\