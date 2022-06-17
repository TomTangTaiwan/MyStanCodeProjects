"""
File: blur.py
Name: Tom Tang
Updated on: 2022/3/15
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def range_limit(x, y, max_width, max_height):
    """
    function to dynamically identify the surrounding pixels

     :param x: coordinate of horizontal line. 3 scenarios: x == 0, x == max width, x in the middle
     :param y: coordinate of vertical line.  3 scenarios: y == 0, y == max width, y in the middle
        1. x == 0 & y == 0: top-left corner, 4 surrounding pixels (incl the target pixel)
        2. x == 0 & y == max height: bottom-left corner, 4 surrounding pixels (incl the target pixel)
        3. x == max width & y == 0: top-right corner, 4 surrounding pixels (incl the target pixel)
        4. x == max width & y == max height: bottom right corner, 4 surrounding pixels (incl the target pixel)
        5. x == 0 & y != 0: left edge, 6 surrounding pixels (incl the target pixel)
        6. x == max width & y != 0: right edge, 6 surrounding pixels (incl the target pixel)
        7. x != 0 & y == 0: top edge, 6 surrounding pixels (incl the target pixel)
        8. x != 0 & y == max height: bottom edge, 6 surrounding pixels (incl the target pixel)
        9. not belongs to above scenario, 9 surrounding pixels (incl the target pixel)

     :param max_width: max width of the image
     :param max_height: max height of the image
     :return:
        i_from: starting point for horizontal line (x)
        i_to: ending point for horizontal line (x)
        j_from: starting point for vertical line (y)
        j_to: ending point for vertical line (y)
        size: the total size of surrounding pixels (should be 4, 6 or 9), also used for calculating the average

     debug syntax:
     limit = range_limit(2, 0, 4, 3)
     for i in range(limit[0], limit[1]):
         for j in range(limit[2], limit[3]):
             print(i, j)
     """
    if x - 1 < 0:
        i_from = 0
    else:
        i_from = x - 1

    if x + 2 > max_width:
        i_to = max_width
    else:
        i_to = x + 2

    if y - 1 < 0:
        j_from = 0
    else:
        j_from = y - 1

    if y + 2 > max_height:
        j_to = max_height
    else:
        j_to = y + 2

    size = (i_to - i_from) * (j_to - j_from)
    return i_from, i_to, j_from, j_to, size


def blur(img):
    """
    :param img: original image
    :return: blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)

    # loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            new_img_p = new_img.get_pixel(x, y)
            max_width = img.width
            max_height = img.height

            # pass value to calculate the upper and lower value of the for loop
            limit = range_limit(x, y, max_width, max_height)

            # var to sum the RGB value from surrounding pixels
            img_p_red = 0
            img_p_green = 0
            img_p_blue = 0
            for i in range(limit[0], limit[1]):
                for j in range(limit[2], limit[3]):
                    img_p = img.get_pixel(i, j)
                    img_p_red += img_p.red
                    img_p_green += img_p.green
                    img_p_blue += img_p.blue

            # averaging the RGB value and return to the target pixel
            new_img_p.red = img_p_red // limit[4]
            new_img_p.green = img_p_green // limit[4]
            new_img_p.blue = img_p_blue // limit[4]

    return new_img


def main():
    """
    1. Get original image
    2. Pass original image to blurring function
    3. Show both original image and blurred image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()

if __name__ == '__main__':
    main()
