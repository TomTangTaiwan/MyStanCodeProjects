"""
File: babygraphics.py
Name: Tom Tang
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    width_max = CANVAS_WIDTH - GRAPH_MARGIN_SIZE * 2
    num_years = len(YEARS)
    width_per_column = width_max // num_years
    x_coordinate = width_per_column * year_index + GRAPH_MARGIN_SIZE
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    x_edge_left = GRAPH_MARGIN_SIZE
    y_edge_top = GRAPH_MARGIN_SIZE
    x_edge_right = CANVAS_WIDTH - GRAPH_MARGIN_SIZE
    y_edge_bottom = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

    # 2 fixed horizontal lines to define top and bottom boundry
    canvas.create_line(x_edge_left, y_edge_top, x_edge_right, y_edge_top)
    canvas.create_line(x_edge_left, y_edge_bottom, x_edge_right, y_edge_bottom)

    for i in range(len(YEARS)):
        x_coord = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coord, 0, x_coord, CANVAS_HEIGHT)
        canvas.create_text(x_coord + TEXT_DX, y_edge_bottom, text=YEARS[i], anchor=tkinter.NW)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # Initialize 'uod'
    # uod = unit of distance between ranks (e.g. rank2 is 1 uod away from rank1)
    uod = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / (MAX_RANK)

    # Step1: Retrieve birth data by looping thru the given name(s) from the name_data
    for name in lookup_names:
        birth_data = name_data[name]
        data_color = COLORS[lookup_names.index(name) % len(COLORS)]  # Data color determinator

        # Initialize 'last' x, y coordinates
        last_x_coord = 0
        last_y_coord = 0

        # Step2: Loop thru each year to identify rank for y coordinate and data label. 
        # Return 1001 as rank or '*' as data label if no data is found.
        for i in range(len(YEARS)):
            if str(YEARS[i]) in birth_data:
                rank = int(birth_data[str(YEARS[i])])
                data_label = f'{name} {rank}'
            else:
                rank = 1001
                data_label = f'{name} *'

            # Step3: Determine x, y coordinates
            x_coord = get_x_coordinate(CANVAS_WIDTH, i)
            y_coord = GRAPH_MARGIN_SIZE + ((rank-1) * uod)

            # Step4-1: Create line starting from 2nd year
            if i != 0:
                canvas.create_line(last_x_coord, last_y_coord, x_coord, y_coord, width=LINE_WIDTH, fill=data_color)
            
            # Step4-2: Create data label
            canvas.create_text(x_coord + TEXT_DX, y_coord, text=data_label, fill=data_color, anchor=tkinter.SW)
            
            # Step5: Store the current x, y coordinates for drawing line in the next loop
            last_x_coord = x_coord
            last_y_coord = y_coord


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
