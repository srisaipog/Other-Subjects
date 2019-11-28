import arcade
from math import sqrt

WIDTH = 640
HEIGHT = 480
BACKGROUND_COLOR = arcade.color.WHITE
TEXT_COLOR = arcade.color.BLACK
TITLE = "The Roller Coaster: Buy it now!"

MAX_HEIGHT = 10
MIN_HEIGHT = 0

window = arcade.open_window(WIDTH, HEIGHT, TITLE)


class Thing:
    def __init__(self, mass, height = 0, velocity = 0):
        self.mass = mass
        self.height = height
        self.velocity = velocity

GRAVITY = 9.8

# e_g = mass * gravity * height
# e_k = 0.5 * mass * (velocity ** 2)

def setup():
    global ball, y
    ball = Thing(5, MAX_HEIGHT, 0)
    y = 5 * HEIGHT / 6

    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.schedule(update, 1/30)
    arcade.run()

   


def update(delta_time):
    pass



@window.event
def on_draw():
    global y, ball
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(WIDTH / 6, y, (WIDTH + HEIGHT) // 100, arcade.color.BLUE)


    if ball.height == 100:
        ball.velocity = 0
    else:
        v1 = 0
        # find v2
        d = (MAX_HEIGHT - ball.height)
        a = 9.8

        v2 = sqrt(v1 ** 2 + 2 * a * d)
    
        ball.velocity = v2


    arcade.draw_text(f"Height: {round(ball.height, 2)} m", 4 * WIDTH / 6, 5 * HEIGHT / 7, TEXT_COLOR)
    arcade.draw_text(f"Mass: {round(ball.mass, 2)} kg", 4 * WIDTH / 6, 4 * HEIGHT / 7, TEXT_COLOR)
    arcade.draw_text(f"Velocity: {round(ball.velocity, 2)} m/s", 4 * WIDTH / 6, 3 * HEIGHT / 7, TEXT_COLOR)
    ek = 0.5 * ball.mass * ball.velocity ** 2
    eg = ball.mass * GRAVITY * ball.height
    
    arcade.draw_text(f"Kinetic Energy: {round(ek, 2)} J", 4 * WIDTH / 6, 2 * HEIGHT / 7, TEXT_COLOR)
    arcade.draw_text(f"Potential Energy: {round(eg, 2)} J", 4 * WIDTH / 6, 1 * HEIGHT / 7, TEXT_COLOR)
    arcade.draw_text(f"Total Energy: {round(ek + eg, 2)} J", 4 * WIDTH / 6, 6 * HEIGHT / 7, TEXT_COLOR)


@window.event
def on_mouse_press(x_mouse, y_mouse, button, modifiers):
    global y
    y = y_mouse

    if y < (HEIGHT / 6):
        y = HEIGHT / 6
    elif y > (5 * HEIGHT / 6):
        y = 5 * HEIGHT / 6
    
    in_max = 5 * HEIGHT / 6
    in_min = HEIGHT / 6

    out_min = MIN_HEIGHT
    out_max = MAX_HEIGHT

    xx = y

    global ball
    ball.height = (xx - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


if __name__ == "__main__":
    setup()
