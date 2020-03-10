import pyaudio
import speech_recognition as sr

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

recog = sr.Recognizer()

with sr.Microphone() as source: #USB Audio device found at device_index=2
 while 1:
  print("Say something!")
  audio = recog.listen(source)
  try:
   print("Google thinks you said " + recog.recognize_google(audio))
  except sr.UnknownValueError:
   print("Google could not understand audio")
  except sr.RequestError as e:
   print("Google error; {0}".format(e))
