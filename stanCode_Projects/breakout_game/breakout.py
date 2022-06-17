"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Tom Tang
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 100			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    num_of_brick_original = graphics.get_num_brick()  # Get the original number of brick
    num_of_brick_removed = 0

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)

        # Start game if game_start == True, and lives is not zero
        if graphics.get_start_signal() and lives != 0:
            graphics.ball.move(graphics.get_speed_x(), graphics.get_speed_y())

            # Collision detection: paddle or brick
            get_obj = graphics.check_collision()
            if get_obj is not None:
                if get_obj == graphics.paddle:
                    # Change dy direction when hitting the paddle top
                    # Change dx direction only when hitting the sides of the paddle
                    # No action when hitting other area of the paddle
                    if graphics.when_collide_paddle() == 'top':
                        graphics.change_direction_dy()
                    elif graphics.when_collide_paddle() == 'side':
                        graphics.change_direction_dx()
                else:
                    # Change dx direction when hitting the side
                    # Otherwise only change dy direction
                    if graphics.when_collide_brick() == 'side':
                        graphics.change_direction_dx()
                    graphics.change_direction_dy()
                    graphics.remove_obj()           # Remove object when hitting bricks
                    num_of_brick_removed += 1       # Count the brick removed

                    # End the game when there's no brick is on screen
                    if num_of_brick_removed == num_of_brick_original:
                        graphics.game_end()
                        break

            # Collision detection: floor, wall, ceiling
            if graphics.is_hit_floor():
                graphics.game_restart()             # Ball back to starting position
                lives -= 1                          # Reduce 1 live when ball hit the floor
            elif graphics.is_hit_wall():
                graphics.change_direction_dx()      # Change dx direction when hitting the either side of the walls
            elif graphics.is_hit_ceiling():
                graphics.change_direction_dy()      # Change dy direction when hitting the ceiling


if __name__ == '__main__':
    main()
