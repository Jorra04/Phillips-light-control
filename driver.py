from controller import Phillips_Hue_Automation
import speech_recognition as sr
import sys
import threading

controller = Phillips_Hue_Automation()
stop_it = False
def callback(recognizer, audio):
    text = '' 
    global stop_it                         
    try:
        text = recognizer.recognize_google(audio)
        print(text)
        if(text == 'terminate' or text == 'Terminate'):
            controller.turn_lamps_off()
            stop_it = True
        if(text == 'Down' or text == 'down'):
            controller.decrease_hue()
        elif(text == 'Up' or text == 'up'):
            controller.increase_hue()
        elif(text == 'Left' or text == 'left'):
            controller.decrease_sat()
        elif(text == 'Right' or text == 'right'):
            controller.increase_sat()
        elif(text == 'Reset' or text == 'reset'):
            controller.reset_vals()
        elif(text == 'Red' or text == 'red'):
            controller.make_colour(0,250)
        elif(text == 'Green' or text == 'green'):
            controller.make_colour(500,120)
        elif(text == 'Purple' or text == 'purple'):
            controller.make_colour(58000,250)
        elif(text == 'On' or text == 'on'):
            controller.turn_lamps_on()
        elif(text == 'Off' or text == 'off'):
            controller.turn_lamps_off()
    except:
        # print("error")
        pass

r = sr.Recognizer()
r.energy_threshold = 4000
r.pause_threshold = 0.8
just_try_and_stop_me = r.listen_in_background(sr.Microphone(), callback)

# [<_MainThread(MainThread, started 164184)>, <Thread(Thread-1, started daemon 164240)>]
import time
while True: 
    if stop_it:
        just_try_and_stop_me(wait_for_stop=True)
        break
    time.sleep(0.1) 