from creds import bridge_ip as ip
from phue import Bridge
import keyboard as kb

__MAX_HUE = 66010
__MAX_SAT = 3250
__MIN_HUE = -40
__MIN_SAT = -30
b = Bridge(ip)
b.connect()

light_name_list = b.get_light_objects('name')

def increase_hue():
    for light in light_name_list:
        if(light_name_list[light].hue + 500 > __MAX_HUE):
            light_name_list[light].hue = __MAX_HUE
        else:
            light_name_list[light].hue += 500
        
def increase_sat():
     
    for light in light_name_list:
        print(light_name_list[light].saturation)

        if(light_name_list[light].saturation + 200 > __MAX_SAT):
            light_name_list[light].saturation = __MAX_SAT
        else:
            light_name_list[light].saturation += 10
            print()


def decrease_hue():
    for light in light_name_list:
        if(light_name_list[light].hue - 500 < __MIN_HUE):
            light_name_list[light].hue = __MIN_HUE
        else:
            light_name_list[light].hue -= 50
def decrease_sat():
    for light in light_name_list:
        if(light_name_list[light].saturation - 115 < __MIN_SAT):
            light_name_list[light].saturation = __MIN_SAT
        else:

            light_name_list[light].saturation -= 50
def reset_vals():
    for light in light_name_list:
        light_name_list[light].hue = 10
        light_name_list[light].saturation = 120
def make_colour(hue, sat):
    for light in light_name_list:
        light_name_list[light].hue = hue
        light_name_list[light].saturation = sat

# escape = False
# while(not escape):
#     if(kb.is_pressed('esc')):
#         break
#     if(kb.is_pressed('down')):
#         decrease_hue()
#     elif(kb.is_pressed('up')):
#         increase_hue()
#     elif(kb.is_pressed('left')):
#         decrease_sat()
#     elif(kb.is_pressed('right')):
#         increase_sat()
#     elif(kb.is_pressed('enter')):
#         reset_vals()
#     elif(kb.is_pressed('r')):
#         make_colour(30,200)
#     elif(kb.is_pressed('g')):
#         make_colour(500,120)
#     elif(kb.is_pressed('b')):
#         make_colour(58000,250)
        
        