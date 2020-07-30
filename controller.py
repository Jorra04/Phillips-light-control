from creds import bridge_ip as ip
from phue import Bridge
import keyboard as kb
class Phillips_Hue_Automation():
    __MAX_HUE = 66010
    __MAX_SAT = 3250
    __MIN_HUE = -40
    __MIN_SAT = -30
    __b = Bridge(ip)
    __b.connect()

    __light_name_list = __b.get_light_objects('name')

    def __init__(self):
        pass
    def increase_hue(self):
        for light in self.__light_name_list:
            if(self.__light_name_list[light].hue + 500 > self.__MAX_HUE):
                self.__light_name_list[light].hue = self.__MAX_HUE
            else:
                self.__light_name_list[light].hue += 500

    def increase_sat(self):

        for light in self.__light_name_list:
            # print(self.__light_name_list[light].saturation)

            if(self.__light_name_list[light].saturation + 200 > self.__MAX_SAT):
                self.__light_name_list[light].saturation = self.__MAX_SAT
            else:
                self.__light_name_list[light].saturation += 10
                print()


    def decrease_hue(self):
        for light in self.__light_name_list:
            if(self.__light_name_list[light].hue - 500 < self.__MIN_HUE):
                self.__light_name_list[light].hue = self.__MIN_HUE
            else:
                self.__light_name_list[light].hue -= 50
    def decrease_sat(self):
        for light in self.__light_name_list:
            if(self.__light_name_list[light].saturation - 115 < self.__MIN_SAT):
                self.__light_name_list[light].saturation = self.__MIN_SAT
            else:

                self.__light_name_list[light].saturation -= 50
    def reset_vals(self):
        for light in self.__light_name_list:
            self.__light_name_list[light].hue = 10
            self.__light_name_list[light].saturation = 120
    def make_colour(self,hue, sat):
        for light in self.__light_name_list:
            self.__light_name_list[light].hue = hue
            self.__light_name_list[light].saturation = sat


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
        controller.make_colour(30,200)
    elif(kb.is_pressed('g')):
        controller.make_colour(500,120)
    elif(kb.is_pressed('b')):
        controller.make_colour(58000,250)
        
        