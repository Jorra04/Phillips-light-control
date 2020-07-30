from controller import Phillips_Hue_Automation
import keyboard as kb

controller = Phillips_Hue_Automation()

escape = False
while(not escape):
    if(kb.is_pressed('esc')):
        break
    if(kb.is_pressed('down')):
        controller.decrease_hue()
    elif(kb.is_pressed('up')):
        controller.increase_hue()
    elif(kb.is_pressed('left')):
        controller.decrease_sat()
    elif(kb.is_pressed('right')):
        controller.increase_sat()
    elif(kb.is_pressed('enter')):
        controller.reset_vals()
    elif(kb.is_pressed('r')):
        controller.make_colour(0,250)
    elif(kb.is_pressed('g')):
        controller.make_colour(500,120)
    elif(kb.is_pressed('b')):
        controller.make_colour(58000,250)
    elif(kb.is_pressed('1')):
        controller.turn_lamps_on()
    elif(kb.is_pressed('0')):
        controller.turn_lamps_off()