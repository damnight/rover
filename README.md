# Shitty_Speech_Rover

driver.py is the main script the runs the rover and depends on
python3.5.3 and the following libs:
  gpiozero
  time
  pyaudio
  speech_recognition

the test-scripts includes
  find_mic.py which spits out the device_index of the registered microphones (requires speech_recognition)

  speech.py runs speech_recognition with Google's Online API, use this to test whether the mic/API works. This is just a reduced form of speechtest.py for clarity

  speechtest.py is the script that comes with speech_recognition, you can comment out the API you don't use in order to test your own.

have fun :)
