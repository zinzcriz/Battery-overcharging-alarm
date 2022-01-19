""" python script to alarm you when your battery is full
Creator:Zinz Criz Xavier
Date:12/11/2021
"""
import psutil #psutil is a cross-platform library for retrieving information on running processes and system utilization in Python. 
import pyttsx3#used here to convert text to speech for the purpose of alarm

import time

# function for converting text to speech
def speak(say):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    engine.setProperty('rate', 175)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)#changing the vocal to female voice(put '0' in place of '1' if you need a male voice)
    engine.say(say)
    engine.runAndWait()

speak("hai...this is a python program to automatically check your battery status and alarm you when it is full")
# retrieves battery information
battery = psutil.sensors_battery()


#retrieves information whether power is plugged or not
n = battery.power_plugged
#checks whether power is plugged.If power is not plugged,asks the user to turn on power.
if(n == 0):
    speak("please turn on your charger for the program to continue")
    print("please turn on your charger for the program to continue")
    #waits 60 secs for you to turn on your charger
    time.sleep(60)
battery = psutil.sensors_battery()
n = battery.power_plugged
#This while loop checks your battery status repeatedly and alerts you when it reaches 99%
while (n == 1):
    percent = battery.percent
    if(percent >= 99):
           speak("battery is full...please unplug your charger ")
           print("Battery percentage remaining: ", battery.percent)
           print("Please unplug your battery")

    time.sleep(60)
    #after a sleep of 60 seconds ,it agains checks whether your power is on or off.If you haven't turned off your charger the loop continues...
    battery = psutil.sensors_battery()
    n = battery.power_plugged




    continue









