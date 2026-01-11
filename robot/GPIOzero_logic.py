from gpiozero import Motor, Robot
import curses
from time import sleep

left_motor = Motor(forward=23, backward=22, enable=25)  # Motor1 pins
right_motor = Motor(forward=17, backward=18, enable=24)  # Motor2 pins

robot = Robot(left=left_motor, right=right_motor)

def test_motors():
    robot.forward()
    sleep(2)
    robot.stop()  

#Uses arrow keys to control the robot
"""actions = {
    curses.KEY_UP: robot.forward,
    curses.KEY_DOWN: robot.backward,
    curses.KEY_LEFT: robot.left,
    curses.KEY_RIGHT: robot.right,
    ord('q'): exit
}"""

actions = {
    ord('w'): robot.forward,
    ord('s'): robot.backward,
    ord('a'): robot.left,
    ord('d'): robot.right,
    ord('q'): exit
}



def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            curses.halfdelay(1)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            robot.stop()
    
if __name__ == "__main__":
    curses.wrapper(main)