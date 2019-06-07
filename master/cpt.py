import random
import math
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Kungfu Chef"


class dropping_food:
    """
    Each instance of this class represents a single snowflake.
    Based on drawing filled-circles.
    """
    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_pos(self):
        # Reset flake to random position above screen
        self.y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
        self.x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        :param width:
        :param height:
        """
        # Calls "__init__" of parent class (arcade.Window) to setup screen
        super().__init__(width, height, title)

        # Sprite lists
        self.food_list = None

    def start_dropping(self):
        """ Set up snowfall and initialize variables. """
        self.food_list = []

        for i in range(1):
            # Create snowflake instance
            food = dropping_food()

            # Randomly position snowflake
            food.x = random.randrange(40,760)
            food.y = (SCREEN_HEIGHT + 20)

            # Set other variables for the snowflake
            food.size = 20

            food.speed = random.randrange(30,60)

            # Add snowflake to snowflake list

            self.food_list.append(food)

        # Don't show the mouse pointer
        self.set_mouse_visible(True)

        # Set the background color
        arcade.set_background_color(arcade.color.COOL_GREY)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command is necessary before drawing
        arcade.start_render()

        # Draw the current position of each snowflake
        for food in self.food_list:
            arcade.draw_circle_filled(food.x, food.y,
                                      food.size, arcade.color.ORANGE)

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """

        # Animate all the snowflakes falling
        for food in self.food_list:
            food.y -= food.speed * delta_time

            # Check if snowflake has fallen below screen
            if food.y < -20:
                food.reset_pos()

            # Some math to make the snowflakes move side to side




def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_dropping()
    arcade.run()

if __name__ == "__main__":
    main()
