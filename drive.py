#!/usr/bin/env python3

"""
File: skidsteer_four_pwm_test.py

This code will test Raspberry Pi GPIO PWM on four GPIO
pins. The code test ran with L298N H-Bridge driver module connected.

Website:	www.bluetin.io
Date:		27/11/2017
"""

__author__ = "Mark Heywood"
__version__ = "0.1.0"
__license__ = "MIT"

from gpiozero import PWMOutputDevice
from time import sleep
import pyaudio
import speech_recognition as sr

#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 19	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 13	# IN1 - Forward Drive
PWM_REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive

# Initialise objects for H-Bridge PWM pins
# Set initial duty cycle to 0 and frequency to 1000
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)


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

def main():
    allStop();
    with sr.Microphone() as source: #USB Audio device found at device_index=2
        recog = sr.Recognizer()
        while 1:
           # try:
           print("Say something!")
           audio = recog.listen(source)
           try:
                line = recog.recognize_google(audio)
                print("Google thinks you said " + line)
                #if not line: break
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
            except sr.UnknownValueError:
               print("Google could not understand audio")
            except sr.RequestError as e:
                print("Google error; {0}".format(e))
    	   # sleep(5)

           # except:
                #print('failed')
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
