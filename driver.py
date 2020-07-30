from controller import Phillips_Hue_Automation
import keyboard as kb
import speech_recognition as sr

r = sr.Recognizer()


controller = Phillips_Hue_Automation()

escape = False
while(not escape):
    text = ''
    try:
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=3)
            text = r.recognize_google(audio_data)
            print(text)
    except:
        pass
    
    if(text == 'terminate' or text == 'Terminate'):
        break
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