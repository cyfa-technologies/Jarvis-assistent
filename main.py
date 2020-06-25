import pyttsx3 # for convert text into audio that speak the function
import datetime # for to know the current system date and time
import speech_recognition as sr # for take the command from the user
import wikipedia # for to search something in wikipedia
import smtplib # for to send email
import  webbrowser as wb # for to search something on the broweser with the help of system browser path
import  os # for to shutdown ,logout,restart the system and play the song
import  random # for to give the random song number
import pyautogui # for to take the screenshot
# from PIL import  Image  for to save a screen shot image inside screen shot folder
import psutil # to figure out the bettery percentage and cpu uses
import pyjokes

# start the pyttsx3 module
engine = pyttsx3.init()

def speak(text):

    engine.say(text)
    engine.runAndWait()

def current_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    print(time)
    speak(time)

def current_date():
    date = datetime.date.today().strftime('%B %d, %Y')
    print(date)
    speak(date)

def date_time():
    Date = datetime.datetime.now().strftime('%B %d, %Y')
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    date_time = "The current date is "+Date + "and th e current time is  " + Time
    speak(date_time)

def wishMe():

    hour = datetime.datetime.now().hour
    print(hour)

    if hour >= 6 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 16:
        speak('Good afternoon')
    elif hour >= 16 and hour <= 22:
        speak('Good evening')
    else:
        speak('Good Night')

    text = 'Hello I am jarvis '
    speak(text)
    speak('what\'s your name sir')
    name = Take_command().capitalize()
    greet = 'hello '+name + 'i am jarvis here please tell me how can i help you'
    speak(greet)

# to exicute this function always connect with internet otherwise it will not be exicuted and it wll give you an error so always connect with the internet before run this
def Take_command():
    # to start the recognizer from the speech_recognition library
    r = sr.Recognizer()
    with sr.Microphone() as source: # for to start the microphone
        print('Listening..')
        r.pause_threshold = 1 # wait for one second after that it will listen the audio
        audio =  r.listen(source) # for get the command from the microphone
    try :
        print('Recognizing...')
        # getting query in the indian english language and auto check from the google
        query = r.recognize_google(audio,language='en-in') # for to get the query
        print(query)
    except Exception as e:
        print(e)
        speak('say that again please')
        return 'None'

    return query

def SendEmail(to,content):
    sever = smtplib.SMTP('smtp.gmail.com',587)
    sever.ehlo()
    sever.starttls()
    sever.login('abcd@gmail.com','123password')
    sever.sendmail('abcd@gmail.com',to,content)
    sever.close()

def screen_shot():
    screen_img = pyautogui.screenshot()
    # img = Image.open(screen_img)
    screen_img.save('C://Users//HP//PycharmProjects//My project//screen shot//ss.png')


def Cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at ' + usage)
    bettery = psutil.sensors_battery().percent
    speak('Your system bettery percentage is ' +str(bettery))
    return bettery

def Tell_jokes():
    speak(pyjokes.get_joke())


if __name__ == '__main__':
    wishMe()
    while True:
        query = Take_command().lower()
        if 'time' in query:
            current_time()

        elif 'date' in query:
            current_date()

        elif 'time and date' in query:
            date_time()

        elif 'wikipedia' in query:
            speak('Searching ....')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=20)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak('What should in say ?')
                content = Take_command()
                to = Take_command()
                SendEmail(to,content)
                speak('Email is succesfully send !')
            except Exception as e:
                print(e)
                speak('unable to send email ! ')

        elif 'search'  in query:
            speak('What should i search ?')
            chrome_path = r'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s'
            search = Take_command().lower()
            wb.get(chrome_path).open_new_tab(search+"")

        elif 'songs' in query:
            songpath = 'F:\\My Songs'
            song_list = os.listdir(songpath)
            random_song = random.randint(0,len(song_list)-1)
            os.startfile(os.path.join(songpath,song_list[random_song]))

        elif 'remember that' in query:
            speak('what should i remember ?')
            data = Take_command()
            speak('you said me to remeber that ' + data)
            remember_file = open('data.txt','w')
            remember_file.write(data)
            remember_file.close()

        elif 'do you know anything' in query:
            with open('data.txt','r') as file:
                data = file.read()
                print(data)
                speak('you said me to remember that ' + data )

        elif 'screenshot' in query:
            screen_shot()
            speak('Done successfully take the screen shot')

        elif 'battery' in query:
            bettery = Cpu()
            if int(bettery) < 20:
                speak('please charge your bettery..')
            else:
                speak('Done..')

        elif query in ['ok','thanks','thank','thank you','thanks you']:
            speak('welcomw sir ,I am always on your service sir')

        elif 'cute' in query or 'beautiful jarvis' in query or 'nice' in query or 'dear' in query:
            print('you are so cool')
            speak('thank you and')
            speak('you are so cool')
            speak('I always here with you for your service .....')

        elif 'joke' in query:
            Tell_jokes()

        elif 'logout' in query:
            os.system('shutdown -l')

        elif 'logout' in query:
            os.system('shutdown /s /t 1')

        elif 'logout' in query:
            os.system('shutdown /r /t 1')

        elif 'offline' in query:
            speak('Thanks you sir')
            print('Thanks you sir')
            quit()


