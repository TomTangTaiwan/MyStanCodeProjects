"""
File: my_drawing
Name: Tom Tang
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Offline Dino

    Hello, I am T-Rex. The extinction taught me one thing:

        Live the moment, leave the phone.

        (I just hope my boss stop looking at phone during the meeting...)
    """
    # open window #
    window = GWindow(1050, 1050)

    # create object - description #
    you_are_offline = GLabel('You are offline.', x=50, y=580)
    device_offline = GLabel('Your internet connection is extinct.', x=50, y=you_are_offline.y + 80)
    trytry = GLabel('Try:', x=50, y=device_offline.y + 60)
    solution1 = GLabel('• Reading a book', x=100, y=trytry.y + 50)
    solution2 = GLabel('• Jogging by the beach', x=solution1.x, y=solution1.y + 50)
    solution3 = GLabel('• Learning Python', x=solution1.x, y=solution2.y + 50)
    error_code = GLabel('ERR_INTERNET_DISCONNECTED', x=trytry.x, y=solution2.y + 100)

    # format object - description #
    # variable
    color_desc = 'dimgray'
    size_title = '-60'
    size_content = '-30'
    size_error = '-20'
    # description
    you_are_offline.font = size_title
    you_are_offline.color = color_desc
    device_offline.font = size_content
    device_offline.color = color_desc
    trytry.font = size_content
    trytry.color = color_desc
    solution1.font = solution2.font = solution3.font = size_content
    solution1.color = solution2.color = solution3.color = color_desc
    error_code.font = size_error
    error_code.color = color_desc

    # create object - background #
    # ground (d = dot, ll = long line, sl = short line)
    grnd = GRect(window.width - 100, 5)
    grnd_d1 = GRect(5, 5)
    grnd_d2 = GRect(5, 5)
    grnd_d3 = GRect(5, 5)
    grnd_d4 = GRect(5, 5)
    grnd_d5 = GRect(5, 5)
    grnd_ll1 = GRect(15, 5)
    grnd_ll2 = GRect(15, 5)
    grnd_ll3 = GRect(15, 5)
    grnd_ll4 = GRect(15, 5)
    grnd_ll5 = GRect(15, 5)
    grnd_sl1 = GRect(10, 5)
    grnd_sl2 = GRect(10, 5)
    grnd_sl3 = GRect(10, 5)
    grnd_sl4 = GRect(10, 5)
    grnd_sl5 = GRect(10, 5)
    # cloud #
    cloud_base = GRect(220, 5)
    cloud_mid1 = GRect(80, 60)
    cloud_left1 = GRect(50, 20)
    cloud_left2 = GRect(10, 40)
    cloud_right1 = GRect(70, 30)
    cloud_right2 = GRect(30, 40)
    cloud_right3 = GRect(10, 20)
    cloud_right4 = GRect(10, 10)
    cloud_mid_c1 = GRect(5, 5)
    cloud_mid_c2 = GRect(5, 5)
    cloud_left_c1 = GRect(5, 5)
    cloud_right_c1 = GRect(10, 5)

    # format object - background #
    # variable
    color_grnd = 'lightgray'
    color_cloud = 'lightgray'
    color_cloud_c = 'white'
    # ground
    grnd.filled = True
    grnd.fill_color = color_grnd
    grnd.color = color_grnd
    grnd_d1.filled = grnd_d2.filled = grnd_d3.filled = grnd_d4.filled = grnd_d5.filled = True
    grnd_d1.fill_color = grnd_d2.fill_color = grnd_d3.fill_color = grnd_d4.fill_color = grnd_d5.fill_color = color_grnd
    grnd_d1.color = grnd_d2.color = grnd_d3.color = grnd_d4.color = grnd_d5.color = color_grnd
    grnd_ll1.filled = grnd_ll2.filled = grnd_ll3.filled = grnd_ll4.filled = grnd_ll5.filled = True
    grnd_sl1.filled = grnd_sl2.filled = grnd_sl3.filled = grnd_sl4.filled = grnd_sl5.filled = True
    # cloud
    cloud_base.filled = True
    cloud_base.fill_color = color_cloud
    cloud_base.color = color_cloud
    cloud_left1.filled = cloud_mid1.filled = cloud_right1.filled = True
    cloud_left1.fill_color = cloud_mid1.fill_color = cloud_right1.fill_color = color_cloud
    cloud_left1.color = cloud_mid1.color = cloud_right1.color = color_cloud
    cloud_left2.filled = cloud_right2.filled = True
    cloud_left2.fill_color = cloud_right2.fill_color = color_cloud
    cloud_left2.color = cloud_right2.color = color_cloud
    cloud_right3.filled = cloud_right4.filled = True
    cloud_right3.fill_color = cloud_right4.fill_color = color_cloud
    cloud_right3.color = cloud_right4.color = color_cloud
    cloud_left_c1.filled = True
    cloud_left_c1.fill_color = color_cloud_c
    cloud_left_c1.color = color_cloud_c
    cloud_mid_c1.filled = cloud_mid_c2.filled = True
    cloud_mid_c1.fill_color = cloud_mid_c2.fill_color = color_cloud_c
    cloud_mid_c1.color = cloud_mid_c2.color = color_cloud_c
    cloud_right_c1.filled = True
    cloud_right_c1.fill_color = color_cloud_c
    cloud_right_c1.color = color_cloud_c

    # create object - dino #
    head = GRect(90, 50)
    head_c1 = GRect(10, 10)
    head_c2 = GRect(10, 10)
    eye = GRect(10, 10)
    mouth = GRect(50, 10)
    jaw = GRect(70, 5)
    neck1 = GRect(40, 5)
    neck2 = GRect(50, 70)
    back = GRect(50, 60)
    back_c1 = GRect(35, 10)
    back_c2 = GRect(20, 10)
    back_c3 = GRect(10, 10)
    butt = GRect(70, 30)
    abdomen = GRect(20, 20)
    abdomen_c1 = GRect(10, 10)
    tail1 = GRect(20, 60)
    tail1_c1 = GRect(10, 10)
    tail1_c2 = GRect(10, 10)
    tail2 = GRect(20, 50)
    tail2_c1 = GRect(10, 10)
    tail3 = GRect(10, 20)
    arm = GRect(20, 10)
    claw = GRect(10, 10)
    left_leg1 = GRect(20, -1)
    left_leg2 = GRect(5, -1)
    left_leg3 = GRect(20, 10)
    right_leg1 = GRect(30, 20)
    right_leg1_c1 = GRect(10, 10)
    right_leg2 = GRect(10, 10)
    right_leg3 = GRect(20, 10)

    # format object - dinosaur #
    # variable
    color_dino = 'dimgray'
    color_dino_eye = 'white'
    color_dino_c = 'white'
    # dino
    head.filled = True
    head.fill_color = color_dino
    head.color = color_dino

    eye.filled = True
    eye.fill_color = color_dino_eye
    eye.color = color_dino_eye

    mouth.filled = jaw.filled = True
    mouth.fill_color = jaw.fill_color = color_dino
    mouth.color = jaw.color = color_dino

    neck1.filled = neck2.filled = True
    neck1.fill_color = neck2.fill_color = color_dino
    neck1.color = neck2.color = color_dino

    back.filled = butt.filled = abdomen.filled = True
    back.fill_color = butt.fill_color = abdomen.fill_color = color_dino
    back.color = butt.color = abdomen.color = color_dino

    arm.filled = claw.filled = True
    arm.fill_color = claw.fill_color = color_dino
    arm.color = claw.color = color_dino

    left_leg1.filled = left_leg2.filled = left_leg3.filled = True
    left_leg1.fill_color = left_leg2.fill_color = left_leg3.fill_color = color_dino
    left_leg1.color = left_leg2.color = left_leg3.color = color_dino

    right_leg1.filled = right_leg2.filled = right_leg3.filled = True
    right_leg1.fill_color = right_leg2.fill_color = right_leg3.fill_color = color_dino
    right_leg1.color = right_leg2.color = right_leg3.color = color_dino

    tail1.filled = tail2.filled = tail3.filled = True
    tail1.fill_color = tail2.fill_color = tail3.fill_color = color_dino
    tail1.color = tail2.color = tail3.color = color_dino

    head_c1.filled = head_c2.filled = True
    head_c1.fill_color = head_c2.fill_color = color_dino_c
    head_c1.color = head_c2.color = color_dino_c

    abdomen_c1.filled = True
    abdomen_c1.fill_color = color_dino_c
    abdomen_c1.color = color_dino_c

    back_c1.filled = back_c2.filled = back_c3.filled = True
    back_c1.fill_color = back_c2.fill_color = back_c3.fill_color = color_dino_c
    back_c1.color = back_c2.color = back_c3.color = color_dino_c

    tail1_c1.filled = tail1_c2.filled = tail2_c1.filled = True
    tail1_c1.fill_color = tail1_c2.fill_color = tail2_c1.fill_color = color_dino_c
    tail1_c1.color = tail1_c2.color = tail2_c1.color = color_dino_c

    right_leg1_c1.filled = True
    right_leg1_c1.fill_color = color_dino_c
    right_leg1_c1.color = color_dino_c

    # create object - cactus
    # br = branch
    mid_br = GRect(40, 230)
    mid_br_c1 = GRect(5, 5)
    mid_br_c2 = GRect(5, 5)
    left_br1 = GRect(40, 25)
    left_br1_c1 = GRect(5, 15)
    left_br1_c2 = GRect(5, 10)
    left_br1_c3 = GRect(5, 5)
    left_br2 = GRect(25, 80)
    left_br2_c1 = GRect(5, 5)
    left_br2_c2 = GRect(5, 5)
    right_br1 = GRect(40, 20)
    right_br1_c1 = GRect(5, 20)
    right_br1_c2 = GRect(5, 15)
    right_br1_c3 = GRect(5, 10)
    right_br1_c4 = GRect(5, 5)
    right_br2 = GRect(25, 90)
    right_br2_c1 = GRect(5, 5)
    right_br2_c2 = GRect(5, 5)

    # format object - cactus #
    # variable
    color_cactus = 'sage'
    color_cactus_c = 'white'
    # cactus
    mid_br.filled = True
    mid_br.fill_color = color_cactus
    mid_br.color = color_cactus

    left_br1.filled = left_br2.filled = True
    left_br1.fill_color = left_br2.fill_color = color_cactus
    left_br1.color = left_br2.color = color_cactus

    right_br1.filled = right_br2.filled = True
    right_br1.fill_color = right_br2.fill_color = color_cactus
    right_br1.color = right_br2.color = color_cactus

    mid_br_c1.filled = mid_br_c2.filled = True
    mid_br_c1.fill_color = mid_br_c2.fill_color = color_cactus_c
    mid_br_c1.color = mid_br_c2.color = color_cactus_c

    left_br2_c1.filled = left_br2_c2.filled = True
    left_br2_c1.fill_color = left_br2_c2.fill_color = color_cactus_c
    left_br2_c1.color = left_br2_c2.color = color_cactus_c

    right_br2_c1.filled = right_br2_c2.filled = True
    right_br2_c1.fill_color = right_br2_c2.fill_color = color_cactus_c
    right_br2_c1.color = right_br2_c2.color = color_cactus_c

    left_br1_c1.filled = left_br1_c2.filled = left_br1_c3.filled = True
    left_br1_c1.fill_color = left_br1_c2.fill_color = left_br1_c3.fill_color = color_cactus_c
    left_br1_c1.color = left_br1_c2.color = left_br1_c3.color = color_cactus_c

    right_br1_c1.filled = right_br1_c2.filled = right_br1_c3.filled = right_br1_c4.filled = True
    right_br1_c1.fill_color = right_br1_c2.fill_color = right_br1_c3.fill_color = right_br1_c4.fill_color = color_cactus_c
    right_br1_c1.color = right_br1_c2.color = right_br1_c3.color = right_br1_c4.color = color_cactus_c

    # place object - description #
    window.add(you_are_offline, x=50, y=580)
    window.add(device_offline, x=50, y=you_are_offline.y + 80)
    window.add(trytry, x=50, y=device_offline.y + 60)
    window.add(solution1, x=100, y=trytry.y + 50)
    window.add(solution2, x=solution1.x, y=solution1.y + 50)
    window.add(solution3, x=solution1.x, y=solution2.y + 50)
    window.add(error_code, x=trytry.x, y=solution2.y + 100)

    # place object - background #
    # ground
    window.add(grnd, x=50, y=370)
    window.add(grnd_d1, x=50, y=grnd.y+35)
    window.add(grnd_d2, x=grnd_d1.x+100, y=grnd.y+20)
    window.add(grnd_d3, x=grnd_d2.x+150, y=grnd.y+10)
    window.add(grnd_d4, x=grnd_d3.x+200, y=grnd.y+40)
    window.add(grnd_d5, x=grnd_d4.x+400, y=grnd.y+30)
    window.add(grnd_ll1, x=100, y=grnd.y+35)
    window.add(grnd_ll2, x=grnd_ll1.x+150, y=grnd.y+20)
    window.add(grnd_ll3, x=grnd_ll2.x+200, y=grnd.y+10)
    window.add(grnd_ll4, x=grnd_ll3.x+400, y=grnd.y+40)
    window.add(grnd_ll5, x=grnd_ll4.x+100, y=grnd.y+30)
    window.add(grnd_sl1, x=70, y=grnd.y+35)
    window.add(grnd_sl2, x=grnd_sl1.x+200, y=grnd.y+20)
    window.add(grnd_sl3, x=grnd_sl2.x+150, y=grnd.y+10)
    window.add(grnd_sl4, x=grnd_sl3.x+100, y=grnd.y+40)
    window.add(grnd_sl5, x=grnd_sl4.x+400, y=grnd.y+30)
    # cloud
    window.add(cloud_base, x=600, y=100)
    window.add(cloud_left1, x=cloud_base.x, y=cloud_base.y-cloud_left1.height)
    window.add(cloud_mid1, x=cloud_left1.x+cloud_left1.width, y=cloud_base.y-cloud_mid1.height)
    window.add(cloud_right1, x=cloud_mid1.x+cloud_mid1.width, y=cloud_base.y-cloud_right1.height)
    window.add(cloud_left2, x=cloud_mid1.x-cloud_left2.width, y=cloud_base.y - cloud_left2.height)
    window.add(cloud_right2, x=cloud_mid1.x + cloud_mid1.width, y=cloud_base.y - cloud_right2.height)
    window.add(cloud_right3, x=cloud_right1.x + cloud_right1.width, y=cloud_base.y - cloud_right3.height)
    window.add(cloud_right4, x=cloud_right3.x + cloud_right3.width, y=cloud_base.y - cloud_right4.height)
    window.add(cloud_left_c1, x=cloud_left1.x, y=cloud_left1.y)
    window.add(cloud_mid_c1, x=cloud_mid1.x, y=cloud_mid1.y)
    window.add(cloud_mid_c2, x=cloud_mid1.x+cloud_mid1.width-cloud_mid_c2.width, y=cloud_mid1.y)
    window.add(cloud_right_c1, x=cloud_right1.x+cloud_right1.width-cloud_right_c1.width, y=cloud_right1.y)

    # place object - dino #
    window.add(head, x=200, y=200)
    window.add(head_c1, x=head.x, y=head.y)
    window.add(head_c2, x=head.x + head.width - 10, y=head.y)

    window.add(eye, x=head.x + 20, y=head.y + 10)

    window.add(mouth, x=head.x, y=head.y + head.height)
    window.add(jaw, x=head.x, y=head.y + head.height + mouth.height)

    window.add(neck1, x=head.x, y=head.y + head.height + mouth.height + jaw.height)
    window.add(neck2, x=head.x - 10, y=head.y + head.height + mouth.height + jaw.height + neck1.height)

    window.add(arm, x=neck2.x+neck2.width, y=neck2.y + 20)
    window.add(claw, x=arm.x + arm.width - 10, y=arm.y + arm.height)

    window.add(back, x=neck2.x - back.width, y=neck2.y + 10)
    window.add(back_c1, x=back.x, y=back.y)
    window.add(back_c2, x=back.x, y=back.y+back_c1.height)
    window.add(back_c3, x=back.x, y=back_c2.y+back_c2.height)

    window.add(butt, x=back.x, y=back.y + back.height)

    window.add(abdomen, x=butt.x+butt.width, y=butt.y)
    window.add(abdomen_c1, x=abdomen.x+10, y=abdomen.y+10)

    window.add(left_leg1, x=butt.x + butt.width - left_leg1.width, y=butt.y + butt.height)
    window.add(left_leg2, x=left_leg1.x + left_leg1.width - left_leg2.width, y=left_leg1.y + left_leg1.height)
    window.add(left_leg3, x=left_leg2.x, y=left_leg2.y + left_leg2.height)

    window.add(right_leg1, x=butt.x + 10, y=butt.y + butt.height)
    window.add(right_leg1_c1, x=right_leg1.x + right_leg1.width - right_leg1_c1.width,
               y=right_leg1.y + right_leg1.height - right_leg1_c1.height)
    window.add(right_leg2, x=right_leg1.x, y=right_leg1.y + right_leg1.height)
    window.add(right_leg3, x=right_leg2.x, y=right_leg2.y + right_leg2.height)

    window.add(tail1, x=back.x-tail1.width, y=back.y+20)
    window.add(tail1_c1, x=tail1.x + tail1.width - tail1_c1.width, y=tail1.y)
    window.add(tail1_c2, x=tail1.x, y=tail1.y + tail1.height - tail1_c2.height)
    window.add(tail2, x=tail1.x - tail2.width, y=tail1.y - 10)
    window.add(tail2_c1, x=tail2.x, y=tail2.y + tail2.height - tail2_c1.height)
    window.add(tail3, x=tail2.x, y=tail2.y - tail3.height)

    # place object - cactus
    window.add(mid_br, x=head.x + 200, y=180)
    window.add(mid_br_c1, x=mid_br.x, y=mid_br.y)
    window.add(mid_br_c2, x=mid_br.x + mid_br.width - mid_br_c2.width, y=mid_br.y)
    window.add(left_br1, x=mid_br.x - left_br1.width, y=mid_br.y + mid_br.height / 5 * 3)
    window.add(left_br2, x=left_br1.x, y=left_br1.y - left_br2.height)
    window.add(left_br1_c1, x=left_br1.x, y=left_br1.y + left_br1.height - left_br1_c1.height)
    window.add(left_br1_c2, x=left_br1_c1.x+left_br1_c1.width,
               y=left_br1_c1.y+left_br1_c1.height-left_br1_c2.height)
    window.add(left_br1_c3, x=left_br1_c2.x + left_br1_c2.width,
               y=left_br1_c1.y+left_br1_c1.height-left_br1_c3.height)
    window.add(left_br2_c1, x=left_br2.x, y=left_br2.y)
    window.add(left_br2_c2, x=left_br2.x + left_br2.width - left_br2_c2.width, y=left_br2.y)
    window.add(right_br1, x=mid_br.x + mid_br.width, y=mid_br.y + mid_br.height / 5 * 3)
    window.add(right_br2, x=right_br1.x + right_br1.width - right_br2.width,
               y=right_br1.y - right_br2.height)
    window.add(right_br1_c1, x=right_br1.x+right_br1.width-right_br1_c1.width,
               y=right_br1.y)
    window.add(right_br1_c2, x=right_br1_c1.x-right_br1_c2.width,
               y=right_br1.y+right_br1.height-right_br1_c2.height)
    window.add(right_br1_c3, x=right_br1_c2.x-right_br1_c3.width,
               y=right_br1.y+right_br1.height-right_br1_c3.height)
    window.add(right_br1_c4, x=right_br1_c3.x-right_br1_c4.width,
               y=right_br1.y+right_br1.height-right_br1_c4.height)
    window.add(right_br2_c1, x=right_br2.x, y=right_br2.y)
    window.add(right_br2_c2, x=right_br2.x + right_br2.width - right_br2_c2.width, y=right_br2.y)


if __name__ == '__main__':
    main()
