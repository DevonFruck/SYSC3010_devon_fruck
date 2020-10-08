from sense_hat import SenseHat
import time
import sys
import os


def pushed_middle(event):

        if event.action == "released":
                print("Exiting...")
                sh.clear()
                os._exit(0)

def pushed_down(event):
        global delay

        if event.action == "pressed":
                if delay > 0.1:
                        delay -= 0.1 # reduces animation delay by 0.1 seconds

def pushed_up(event):
        global delay

        if event.action == "pressed":
                if delay < 3:
                        delay += 0.1 #increases animation delay by 0.1 seconds
                



delay = 1.5 # default time delay for animation in seconds
sh = SenseHat()
sh.stick.direction_middle = pushed_middle
sh.stick.direction_down = pushed_down
sh.stick.direction_up = pushed_up
        
while True:       
        
        sh.load_image("1.png")
        time.sleep(delay)
        sh.load_image("4.png")
        time.sleep(delay)
        sh.load_image("3.png")
        time.sleep(delay)
        sh.load_image("2.png")

                


	
#for event in sh.stick.get_events():
 #       print("Joystick go vroom")			
        #sh.clear();
