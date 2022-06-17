"""
File: bouncing_ball
Name: Tom Tang
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# CONSTANT
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# global variable
window = GWindow(800, 500, title='bouncing_ball.py')
oval = GOval(SIZE, SIZE)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    oval.filled = True
    window.add(oval, x=START_X, y=START_Y)
    onmouseclicked(release)


def release(event):
    """
    1. oval.y + SIZE <= window.height or speed_drop <= 0 ---> drop
    without checking speed_drop is still negative, the 1st y coordinate + oval's diameter
    right after the rebound might still exceed the window.height

    2. 'vy' change signage when hit the window.height, adding 'GRAVITY' until it hits zero
    'vy' = y velocity

    3. mouse click only effects when oval is at the starting point and 'count' < 3
    p.s. 'count' need to be global variable otherwise it reverts to zero after every break

    4. Once the oval hit the window.width, return to starting coordinates
    """
    global count
    vy = 0
    if oval.x == START_X and oval.y == START_Y and count < 3:
        while True:
            if oval.x + SIZE >= window.width:
                break
            else:
                if oval.y + SIZE <= window.height or vy <= 0:
                    vy += GRAVITY
                else:
                    vy = -vy * REDUCE
                oval.move(VX, vy)
                pause(DELAY)
        window.add(oval, x=START_X, y=START_Y)
        count += 1


if __name__ == "__main__":
    main()
