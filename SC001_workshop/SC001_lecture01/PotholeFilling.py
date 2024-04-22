"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    """
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()

def go_in():
    """
    pre condition:Karel is at the upper left,facing east.
    post condition:Karel is in the pothole,facing south.
    """
    move()
    turn_right()
    move()

def go_out():
    """
    pre condition:Karel is in the pothole,facing south.
    post condition:Karel is at the next upper left,facing east.
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()

def put_99_beepers():
    for i in range(99):
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
