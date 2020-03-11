#!/usr/bin/env python3

#My code is adapted from:
"""
File: skidsteer_four_pwm_test.py

This code will test Raspberry Pi GPIO PWM on four GPIO
pins. The code test ran with L298N H-Bridge driver module connected.

Website:    www.bluetin.io
Date:       27/11/2017
"""
__authors__ = "Mark Heywood"
__version__ = "0.1.0"
__license__ = "MIT"
#I used his functions for movement



from gpiozero import PWMOutputDevice
from time import sleep
import pyaudio
import speech_recognition as sr

#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 13   # IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 6   # IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 26  # IN1 - Forward Drive
PWM_REVERSE_RIGHT_PIN = 19   # IN2 - Reverse Drive

# Initialise objects for H-Bridge PWM pins
# Set initial duty cycle to 0 and frequency to 1000
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 2000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 2000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 2000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 2000)


def allStop():
    forwardLeft.value = 0
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 0

def forwardDrive():
    forwardLeft.value = 1.0
    reverseLeft.value = 0
    forwardRight.value = 1.0
    reverseRight.value = 0

def reverseDrive():
    forwardLeft.value = 0
    reverseLeft.value = 1.0
    forwardRight.value = 0
    reverseRight.value = 1.0

def spinLeft():
    forwardLeft.value = 0
    reverseLeft.value = 1.0
    forwardRight.value = 1.0
    reverseRight.value = 0

def spinRight():
    forwardLeft.value = 1.0
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 1.0

def forwardTurnLeft():
    forwardLeft.value = 0.2
    reverseLeft.value = 0
    forwardRight.value = 0.8
    reverseRight.value = 0

def forwardTurnRight():
    forwardLeft.value = 0.8
    reverseLeft.value = 0
    forwardRight.value = 0.2
    reverseRight.value = 0

def reverseTurnLeft():
    forwardLeft.value = 0
    reverseLeft.value = 0.2
    forwardRight.value = 0
    reverseRight.value = 0.8

def reverseTurnRight():
    forwardLeft.value = 0
    reverseLeft.value = 0.8
    forwardRight.value = 0
    reverseRight.value = 0.2

#This is the stuff I wrote myself
def main():
    #make sure motors aren't running wild
    allStop();
    with sr.Microphone() as source: #set the Mircophone to source (you may need to write Microphone(device_index=1) where 1 is the index of your microphone
                                    #you can query it by using the script in the test-scripts folder
        recog = sr.Recognizer()                   #refer to speech_recognition documentation. these settings are real-world environment dependent
        recog.energy_threshold = 200
        recog.pause_threshold = 0.3
        recog.phrase_threshold = 0.3
        recog.non_speaking_duration = 0.3
        recog.phrase_timeout = 1
        recog.dynamic_energy_threshold = False #added this because otherwise the threshold would lower so much, that it only registered the motors, getting stuck in endless recording
        line ='' #init line
        while line != 'exit': #exit the program by saying exit
            #you can use the console to check what the API returned
            print("Awaiting your command")
            audio = recog.listen(source)
            try:
                    line = recog.recognize_google(audio) #use your preferred API here
                    print("Right on, " + line + "!!!")
                    #simple if clauses to which map the word saved in line to the correct driving function
                    if line == 'forward':
                            forwardDrive()
                    if line == 'reverse':
                            reverseDrive()
                    if line == 'spin left':
                            spinLeft()
                    if line == 'spin right':
                            spinRight()
                    if line == 'left':
                            forwardTurnLeft()
                    if line == 'right':
                            forwardTurnRight()
                    if line == 'reverse left':
                            reverseTurnLeft()
                    if line == 'reverse right':
                            reverseTurnRight()
                    if line == 'stop':
                            allStop()
            #possible errors
            except sr.UnknownValueError:
                print("Google could not understand audio")
            except sr.RequestError as e:
                print("Google error; {0}".format(e))
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
