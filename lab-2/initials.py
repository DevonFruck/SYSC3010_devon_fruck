from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

white = (255,255,255)
nothing = (0,0,0)

def D():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, O, O, O, O,
    O, W, O, O, W, O, O, O,
    O, W, O, O, O, W, O, O,
    O, W, O, O, O, W, O, O,
    O, W, O, O, O, W, O, O,
    O, W, O, O, W, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo

def F():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, O, O,
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, W, W, W, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    ]
    return logo

# This function is called when any joystick action is input
def pushed_any(event):
    global count

    # ensures action does not trigger on depress
    if event.action == "pressed":
        count += 1
        s.set_pixels(images[count % len(images)]())


s.stick.direction_any = pushed_any # mapping joystick movement to function
images = [D, F]
count = 0

s.set_pixels(D()) # initially set to "D"

while True: 
    time.sleep(1) # Loop so code doesn't end 
