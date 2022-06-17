"""
File: sierpinski.py
Name: Tom Tang
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                 # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: How many layers of triangle we need to draw
	:param length: To determine the size of the biggest triangle (order 1 triangle)
	:param upper_left_x: The x coordinate of the order 1 triangle
	:param upper_left_y: The y coordinate of the order 1 triangle
	:return: A sierpinski triangle with given 'orders'
	"""
	s1 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
	s2 = GLine(upper_left_x, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
	s3 = GLine(upper_left_x+length, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
	window.add(s1)
	window.add(s2)
	window.add(s3)
	sierpinski_triangle_helper(order, length/2, upper_left_x+length/2, upper_left_y)


def sierpinski_triangle_helper(order, length, middle_x, middle_y):
	# Base case
	if order == 1:
		pass
	# Recursion
	else:
		s_left = GLine(middle_x, middle_y, middle_x-length/2, middle_y+length*0.866)
		s_right = GLine(middle_x, middle_y, middle_x+length/2, middle_y+length*0.866)
		s_bottom = GLine(middle_x-length/2, middle_y+length*0.866, middle_x+length/2, middle_y+length*0.866)
		window.add(s_left)
		window.add(s_right)
		window.add(s_bottom)
		sierpinski_triangle_helper(order-1, length/2, middle_x-length/2, middle_y)
		sierpinski_triangle_helper(order-1, length/2, middle_x+length/2, middle_y)
		sierpinski_triangle_helper(order-1, length/2, middle_x, middle_y+length*0.866)


if __name__ == '__main__':
	main()