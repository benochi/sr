import speech_recognition as sr
import pyttsx3

#initialize the recognizer
r = sr.Recognizer()

#convert text to speech
def speakText(command):
  engine = pyttsx3.init()
  engine.say(command)
  engine.runAndWait()

#use mcirophone as source for input
with sr.Microphone() as source2:
  #brief pause to adjust for surrounding volume
  r.adjust_for_ambient_noise(source2, duration=0.1)
  speakText("What is your name?")
  #listen for user input
  audio2 = r.listen(source2)
  #use google to recognize audio
  try:
    userInput = r.recognize_google(audio2)
    userInput = userInput.lower()
    speakText("your name is " + userInput)
  except:
    speakText("No user input was heard.  Check your microphone and try again.")
  
  