"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()

def jump():
    """
    Pre-condition:Karel is on the left side of the wall,facing east.
    Post-condition:Karel is on the right side of the wall.
    """
    while not front_is_clear():
        turn_left()
        #facing north
        move()
        turn_right()
        #facing east
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
