#========================
# By: Mizuky
# This is pomodoro clock
# More about: https://en.m.wikipedia.org/wiki/Pomodoro_Technique
#========================

import time
import os
from pygame import mixer 

clear = lambda: os.system('cls')
music = r'C:\Users\Mizuky\Documents\.Programação\Python\PomodoroClock\files\alarm.wav'
workTime = [600, 1200, 1800, 2400, 3000, 3600] #10 minutes, 20, ... in seconds
workTimeM = [10, 20, 30, 40, 50, 60] #The choices in minutes
breakTime = [300, 600, 900] #5 minutes, 10, ... in seconds
breakTimeM = [5, 10, 15] #The choices in minutes
clear()

print('''  _____                          _                 
 |  __ \                        | |                
 | |__) |__  _ __ ___   ___   __| | ___  _ __ ___  
 |  ___/ _ \| '_ ` _ \ / _ \ / _` |/ _ \| '__/ _ \ 
 | |  | (_) | | | | | | (_) | (_| | (_) | | | (_) |
 |_|   \___/|_| |_| |_|\___/ \__,_|\___/|_|  \___/''')
print('''                           _____ _            _    _ 
                          / ____| |          | |  | |
                         | |    | | ___   ___| | _| |
                         | |    | |/ _ \ / __| |/ / |
                         | |____| | (_) | (__|   <|_|
                          \_____|_|\___/ \___|_|\_(_)
''')

print(" Choose the work time:\n")
print(" [1] 10 minutes")
print(" [2] 20 minutes")
print(" [3] 30 minutes")
print(" [4] 40 minutes")
print(" [5] 50 minutes")
print(" [6] 60 minutes")
workChoose = input("\n Choose: ")
clear()
print("\n Choose the break time:\n")
print(" [1] 5 minutes")
print(" [2] 10 minutes")
print(" [3] 15 minutes")
breakChoose = input("\n Choose: ")

if workChoose == "1":
    tW = workTime[0]
    tWM = workTimeM[0]
elif workChoose == "2":
    tW = workTime[1]
    tWM = workTimeM[1]
elif workChoose == "3":
    tW = workTime[2]
    tWM = workTimeM[2]
elif workChoose == "4":
    tW = workTime[3]
    tWM = workTimeM[3]
elif workChoose == "5":
    tW = workTime[4]
    tWM = workTimeM[4]
elif workChoose == "6":
    tW = workTime[5]
    tWM = workTimeM[5]
else:
    print("Invalid choice!")

if breakChoose == "1":
    tB = breakTime[0]
    tBM = breakTimeM[0]
elif breakChoose == "2":
    tB = breakTime[1]
    tBM = breakTimeM[1]
elif breakChoose == "3":
    tB = breakTime[2]
    tBM = breakTimeM[2]
else:
    print(" Invalid choice!")

clear()

mixer.init()
mixer.music.load(music)

def countdown(t, t2): #The counter
    while t: #Work time
        clear()
        print("\n Work time!!\n")
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(" Time: " + timeformat, end='\r')
        print(f"\n\n\n\n\n\n\n\n\n Chooses: \n Work time: {tWM} minutes \n Break time: {tBM} minutes")
        time.sleep(1)
        t -= 1
    
    mixer.music.play(0)
    while t2: #Break time
        clear()
        print("\n Break time!!\n")
        mins, secs = divmod(t2, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(" Time: " + timeformat, end='\r')
        print(f"\n\n\n\n\n\n\n\n\n Chooses: \n Work time: {tWM} minutes \n Break time: {tBM} minutes")
        time.sleep(1)
        t2 -= 1
    mixer.music.play(0)

countdown(tW, tB)
