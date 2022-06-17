"""
File: draw_line
Name: Tom Tang
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# CONSTANT
SIZE = 5
RADIUS = SIZE/2

# global variable
window = GWindow()
oval = GOval(SIZE, SIZE)
gobj = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(event):
    """
    use 'gboj' check if the oval has been placed
        no: place oval
        yes: draw the line based on center of oval on window and the center of mouse cursor

    Lesson learnt:
    1. oval.x and oval.y only point at the top-left coordinate of the object. If the object is an oval, the coordinate
    is outside the oval, so the code can't locate the oval with window.get_object_at.
    So we need to add the radius to appointed coordinates to be on top of the oval.
    """
    global gobj
    gobj = window.get_object_at(oval.x + RADIUS, oval.y + RADIUS)
    if gobj is not None:
        line = GLine(oval.x - RADIUS, oval.y - RADIUS, event.x - RADIUS, event.y - RADIUS)
        window.add(line)
        window.remove(oval)
        gobj = None
    else:
        window.add(oval, x=event.x - RADIUS, y=event.y - RADIUS)


if __name__ == "__main__":
    main()
