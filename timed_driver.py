from controller import Phillips_Hue_Automation
from datetime import datetime as dt
controller = Phillips_Hue_Automation()

print(dt.now().hour)


while True:
    if dt.now().hour == 20:
        controller.all_lights_on()
    elif dt.now().hour == 11:
        controller.turn_lamps_off()