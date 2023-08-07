from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3 #speech to text conversion
import speech_recognition as sr #recognize speech with help microphone and also we can use gtss
import os #for run desktop application
import time #tell time
import webbrowser 
import datetime
import pywhatkit
import wikipedia
import pyjokes
import webbrowser 
import random #random advice or rondom selection from the data 
import wolframalpha # for give  answer in mathematics geography and science question 
import subprocess #use to restart, shutdown, sleep  the system and more
import json #( JavaScript Object Noatation )interchange the lightweight information
import requests #request the HTTP request
import smtplib # sending email
from urllib.request import urlopen   #for opening url
from bs4 import BeautifulSoup  #exracting data from  HTML and XML file  and parsing the file.
import shutil # to create the file in read and wirte mode.


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wish():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour <12:
		speak("Good morning")
	elif hour>=12 and hour<18:
		speak("Good Afternoon")
	else:
		speak("Good night")

def send_whatsapp_message(number, message):
	pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)

def get_random_advice():
	res = requests.get("https://api.adviceslip.com/advice").json()
	return res['slip']['advice']

def sendEmail(to, content):
	print("Sending mail to ", to)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	#paste your email id and password in the respective places
	server.login('your email id', 'password') 
	server.sendmail('your email id', to, content)
	server.close()
	
def getWeather(city_name):
	#cityName=place.get() #getting input of name of the place from user
	baseUrl = "http://api.openweathermap.org/data/2.5/weather?" #base url from where we extract weather report
	url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  
	response = requests.get(url)
	x = response.json()

	#If there is no error, getting all the weather conditions
	if x["cod"] != "404":
		y = x["main"]
		temp = y["temp"]
		temp-=273 
		pressure = y["pressure"]
		humidity = y["humidity"]
		z = x["weather"]
		description = z[0]["description"]
		info=(" Temperature= " +str(temp)+"°C"+"\n atmospheric pressure (hPa) ="+str(pressure) +"\n humidity = " +str(humidity)+"%" +"\n description = " +str(description))
		print(info)
		speak("Here is the weather report at")
		speak(city_name)
		speak(info)
	else:
		speak(" City Not Found ")

def getNews():
	try:
		response = requests.get('https://timesofindia.indiatimes.com/news')
		b4soup = BeautifulSoup(response.text, 'html.parser')
		headLines = b4soup.find('body').find_all('h3')
		unwantedLines = ['BBC World News TV', 'BBC World Service Radio',
					'News daily newsletter', 'Mobile app', 'Get in touch']

		for x in list(dict.fromkeys(headLines)):
			if x.text.strip() not in unwantedLines:
				print(x.text.strip())
	except Exception as e:
		print(str(e))


paths = {
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_cmd():
	os.system('start cmd')
def open_camera():
	subprocess.run('start microsoft.windows.camera:', shell=True)
def open_calculator():
	subprocess.Popen(paths['calculator'])



class mainT(QThread):
	def __init__(self):
		super(mainT,self).__init__()
	
	def run(self):
		self.PATRICK()
	
	def STT(self):
		R = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...........")
			R.pause_threshold = 1
			R.energy_threshold=600
			audio = R.listen(source)
		try:
			print("Recogn......")
			text = R.recognize_google(audio,language='en-in')
			print(">> ",text)
		except Exception:
			speak("Sorry Speak Again")
			return "None"
		text = text.lower()
		return text
	def PATRICK(self):
		wish()
		while True:
			self.query = self.STT()
			if 'good bye' in self.query:
				sys.exit()
			elif 'open google' in self.query:
				webbrowser.open('www.google.co.in')
				speak("opening google")
			elif 'open youtube' in self.query:
				webbrowser.open("www.youtube.com")
			elif 'play music' in self.query:
				speak("playing music from pc")
				self.music_dir ='C:\\Users\\TH. HIMANSHU SINGH\\Music'
				self.musics = os.listdir(self.music_dir)
				os.startfile(os.path.join(self.music_dir,self.musics[0]))
			
			elif 'time' in self.query:
			
				time = datetime.datetime.now().strftime('%I:%M %p')
				print(time)
				speak('Current time is ' + time)
			elif 'date' in self.query:
				date = datetime.datetime.now().strftime('%d /%m /%y')
				print(date)
				speak('Todays date is ' + date)
				
			elif 'wikipedia' in self.query:
				person = self.query.replace('wikipedia', '')
				info = wikipedia.summary(person, 2)
				print(info)
				speak(info)
			elif 'joke' in self.query:
				speak(pyjokes.get_joke())
			
			elif 'open youtube' in self.query:
				webbrowser.open("youtube.com")
					
			elif 'open google' in self.query:
				webbrowser.open("google.com")

			elif 'message ' in self.query or 'whatsapp' in self.query:
				speak('whom u want to send message')
				number = self.STT()
				speak('what message u want to send ')
				message= self.STT()
				send_whatsapp_message(number, message)
				speak('sending message')
				print("Successfully Sent!")
			elif "open cmd" in self.query or "open command prompt" in self.query:
				speak("Opening command prompt sir")
				open_cmd()
			elif "camera" in self.query:
				speak("Opening camera sir")
				open_camera()
			elif "calculator" in self.query:
				speak("Opening calculator sir")
				open_calculator()

			elif 'play ' in self.query:
				song = self.query.replace('play', '')
				speak('playing ' + song)
				pywhatkit.playonyt(song)
			# SOME NLU QUESTION		
			elif 'how are you' in self.query or 'how have you been' in self.query :
				speak("I am doing Excellent . Just got a new home in your PC.")
					
			elif 'what are you doing' in self.query:
					speak("I am here speaking to you. That's what I am doing")
			
			elif 'what am i doing' in self.query:
				speak("You tell me. My guess is you are speaking to me")        
			elif 'how is life' in self.query or 'how is your life' in self.query:
				speak("Life in the silicon world is amazing")
				
			elif 'where do you live' in self.query or 'where do you stay' in self.query or 'where is your home' in self.query or 'what is your address' in self.query:
				speak('I live in the silicon world. Be born next time as a software. Then you can come live with me too')
				
			elif 'whom am I speaking to' in self.query:
				speak("You are speaking to PATRICK ")

				
			elif 'who created you' in self.query or 'who made you' in self.query or 'who is your creator' in self.query or "who's creation are you" in self.query or 'who has made you' in self.query or 'who has created you' in self.query:
				speak('I was created by Naman  with the helpful suggestions from Himanshu and Zubair  which helped in how I turned out to be.')
				
			elif 'your birthday' in self.query or 'when were you created' in self.query or 'when were you born' in self.query:
				speak('I am a work in progress always.')
				
				
			elif 'what is your name' in self.query or 'what should I call you' in self.query or \
							"what's your name" in self.query:
				speak("I am PATRICK")
				
			# elif 'to whom do you belong' in self.query or 'who is your owner' in self.query:
			#     speak("I am owned and copyrighted by "+ user_name)
			elif "will you be my gf" in self.query or "will you be my bf" in self.query:
				speak("I'm not sure about that, may be you should give me some time")
			elif "i love you" in self.query:
				speak("Thank you! But, It's a pleasure to hear it from you.")
			elif 'joke' in self.query:
				speak(pyjokes.get_joke())
					
			elif 'mail' in self.query:
				try:
					speak("Whom should I send the mail")
					to = self.query()
					speak("What is the body?")
					content = self.query()
					sendEmail(to, content)
					speak("Email has been sent successfully !")
				except Exception as e:
					print(e)
					speak("I am sorry, not able to send this email")

			elif 'exit' in self.query or 'Thankyou' in self.query:
				speak("Thanks for giving me your time")
				sys.exit()

			elif "weather" in self.query:
				speak(" Please tell your city name ")
				print("City name : ")
				cityName = self.STT()
				getWeather(cityName)

			elif "what is" in self.query or "who is" in self.query:
					
				client = wolframalpha.Client("API_ID")
				res = client.query(self.query)

				try:
					print (next(res.results).text)
					speak (next(res.results).text)
				except StopIteration:
					print ("No results")


			elif 'search' in self.query or 'find' in self.query:
				self.query = self.query.replace("search", "")
				pywhatkit.search(self.query)

			elif 'news' in self.query:
				getNews()
				
			elif "don't listen" in self.query or "stop listening" in self.query:
				speak("for how long you want me to stop listening self.querys")
				a = int(self.STT())
				time.sleep(a)
				print(a)
					
			elif 'shutdown system' in self.query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')

			elif "restart" in self.query:
				subprocess.call(["restart", "/r"])


			elif "sleep" in self.query:
				speak("Setting in sleep mode")
				subprocess.call("sleep / h")
				
			elif "advice" in self.query:
				speak(f"Here's an advice for you, sir")
				advice = get_random_advice()
				speak(advice)
				speak("For your convenience, I am printing it on the screen sir.")
				print(advice)

			elif "write a note" in self.query:
				speak("What should i write, sir")
				note = self.STT()
				file = open('PATRICK.txt', 'w')
				speak("Sir, Should i include date and time")
				snfm = self.STT()
				if 'yes' in snfm or 'sure' in snfm:
					strTime = datetime.datetime.now().strftime("% H:% M:% S")
					file.write(strTime)
					file.write(" :- ")
					file.write(note)
				else:
					file.write(note)



FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
	def __init__(self,parent=None):
		super(Main,self).__init__(parent)
		self.setupUi(self)
		self.setFixedSize(1920,1080)
		self.label_7 = QLabel
		self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
		"border:none;")
		self.exitB.clicked.connect(self.close)
		self.setWindowFlags(flags)
		Dspeak = mainT()
		self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
		self.label_7.setCacheMode(QMovie.CacheAll)
		self.label_4.setMovie(self.label_7)
		self.label_7.start()

		self.ts = time.strftime("%A, %d %B")

		Dspeak.start()
		self.label.setPixmap(QPixmap("./lib/tuse.png"))
		self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
		self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())