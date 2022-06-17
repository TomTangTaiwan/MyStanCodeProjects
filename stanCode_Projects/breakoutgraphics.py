"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Name: Tom Tang
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 5    # Initial vertical speed for the ball 7
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Default instance variable
        self.paddle_offset = paddle_offset     # store paddle_offset to self
        self.get_obj = None                    # Default variable for getting object
        self.start = False                     # Game switch

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        self.start_x = self.ball.x       # Store ball start position: x
        self.start_y = self.ball.y       # Store ball start position: y
        self.ball_x = self.ball.x        # Default value for ball position: x
        self.ball_y = self.ball.y        # Default value for ball position: y

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.game_start)

        # Draw bricks
        self.num_of_brick = brick_cols * brick_rows
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height,
                              x=0 + i * (brick_width + brick_spacing),
                              y=brick_offset + j * (brick_height + brick_spacing))
                brick.filled = True
                # Paint different color based on the number of row
                if j+1 <= brick_rows * 0.2:
                    color = 'red'
                elif j+1 <= brick_rows * 0.4:
                    color = 'orange'
                elif j+1 <= brick_rows * 0.6:
                    color = 'yellow'
                elif j+1 <= brick_rows * 0.8:
                    color = 'green'
                else:
                    color = 'blue'
                brick.fill_color = color
                brick.color = color
                self.window.add(brick)

    # Actions
    def move_paddle(self, event):
        """
        :param event: mouse event, when mouse moved
        :return: move paddle to where mouse is pointing
        """
        if event.x - self.paddle.width/2 < 0:
            self.paddle.x = 0
        elif event.x + self.paddle.width/2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2

    def game_start(self, event):
        """
        :param event: mouse event, when mouse clicked, not used in the method
        :return: set start = True to start the game
        """
        self.start = True

    def game_restart(self):
        """
        :return: reset start = False and the ball to start position
        """
        self.start = False
        self.window.add(self.ball, x=self.start_x, y=self.start_y)

    def game_end(self):
        """
        :return: set start = False to end the game
        """
        self.start = False

    def change_direction_dx(self):
        """
        :return: change ball.move dx to the opposite direction
        """
        self.__dx = -self.__dx

    def change_direction_dy(self):
        """
        :return: change ball.move dy to the opposite direction
        """
        self.__dy = -self.__dy

    def remove_obj(self):
        """
        :return: remove object gotten from collision
        """
        self.window.remove(self.get_obj)

    # Conditions
    def is_hit_wall(self):
        """
        :return: check if ball hits either side of walls
        """
        return self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width

    def is_hit_ceiling(self):
        """
        :return: check if ball hits the ceiling
        """
        return self.ball.y <= 0

    def is_hit_floor(self):
        """
        :return: check if ball hits the floor (reduce live in next action)
        """
        return self.ball.y + self.ball.height >= self.window.height

    def check_collision(self):
        """
        :return: collision detection, return the object captured or None if no object is collided
        """
        for x in range(2):
            for y in range(2):
                self.ball_x = self.ball.x + self.ball.width * x
                self.ball_y = self.ball.y + self.ball.height * y
                self.get_obj = self.window.get_object_at(self.ball_x, self.ball_y)
                if self.get_obj is not None:
                    return self.get_obj

    def when_collide_paddle(self):
        """
        :return: check the ball hits which side of the paddle to determine the following action
            top: change ball.move dy's direction, dx no change
            side: change ball.move dx's direction, dy no change
            others: no change for both dy and dx

            The threshold is to set up areas on the paddle where program allows overlap (ball and paddle)
            Otherwise, ball easily stuck in/under paddle when paddle is moving fast
        """
        # Threshold of tolerance range/area when ball overlaps the paddle
        threshold_x = self.paddle.width * 0.1
        threshold_y = self.paddle.height * 0.2

        # Check if collision point is the bottom point of the ball
        is_bottom_point = self.ball_y != self.ball.y

        # Default x and y coordinates for drawing top/side areas
        x = self.paddle.x
        xw = self.paddle.x + self.paddle.width
        x1 = self.paddle.x + threshold_x
        x2 = self.paddle.x + self.paddle.width - threshold_x
        y = self.paddle.y
        yh = self.paddle.y + self.paddle.height
        y1 = self.paddle.y + threshold_y
        y2 = self.paddle.y + self.paddle.height - threshold_y

        # Logics to determine is top or side area collided
        if x <= self.ball_x <= xw and y <= self.ball_y <= y1 and is_bottom_point:
            result = 'top'
        elif (x <= self.ball_x <= x1 and y1 <= self.ball_y <= y2) \
                or (x2 <= self.ball_x <= xw and y1 <= self.ball_y <= y2):
            result = 'side'
        else:
            result = None
        return result

    def when_collide_brick(self):
        """
        :return: check the ball hits which side of the brick to determine the following action
            top/bottom: change ball.move dy direction, dx no change
            side: change ball.move dx direction, dy no change
            others: no change for both dy and dx
        """
        # Threshold of tolerance range/area when ball overlaps the brick
        threshold_x = self.get_obj.width * 0.1
        threshold_y = self.get_obj.height * 0.1

        # Check if collision point is the top/bottom point of the ball
        is_top_point = self.ball_y != self.ball.y
        is_bottom_point = self.ball_y != self.ball.y

        # Default x and y coordinates for drawing top/side areas
        x = self.get_obj.x
        xw = self.get_obj.x + self.get_obj.width
        x1 = self.get_obj.x + threshold_x
        x2 = self.get_obj.x + self.get_obj.width - threshold_x
        y = self.get_obj.y
        yh = self.get_obj.y + self.get_obj.height
        y1 = self.get_obj.y + threshold_y
        y2 = self.get_obj.y + self.get_obj.height - threshold_y

        # Logics to determine is top or side area collided
        if x <= self.ball_x <= xw and y <= self.ball_y <= y1 and is_bottom_point:
            result = 'top'
        elif x <= self.ball_x <= xw and y2 <= self.ball_y <= yh and is_top_point:
            result = 'bottom'
        elif (x <= self.ball_x <= x1 and y1 <= self.ball_y <= y2) \
                or (x2 <= self.ball_x <= xw and y1 <= self.ball_y <= y2):
            result = 'side'
        else:
            result = None
        return result

    # getter
    def get_start_signal(self):
        return self.start

    def get_speed_x(self):
        return self.__dx

    def get_speed_y(self):
        return self.__dy

    def get_num_brick(self):
        return self.num_of_brick
