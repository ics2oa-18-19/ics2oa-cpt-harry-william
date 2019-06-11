import random
import arcade
import math
import os
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Kungfu Chef"
tile_img1 = arcade.load_texture('/home/robuntu/xia/classwork/acade/5x7ft-vinyl-digital-chinese-kongfu-karate.jpg')
tile_img2 = arcade.load_texture('/home/robuntu/xia/classwork/acade/image url.png')


class Food:
    """
    Each instance of this class represents a single food.
    Based on drawing filled-circles.
    """
    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_pos(self):
        # Reset flake to random position above screen
        self.y = (SCREEN_HEIGHT + 20)
        self.x = random.randrange(20,SCREEN_WIDTH-20)


class MyGame(arcade.Window):


    def __init__(self, width, height, title):
        # Calls "__init__" of parent class (arcade.Window) to setup screen
        super().__init__(width, height, title)

        # Sprite lists
        arcade.set_background_color(arcade.color.COOL_GREY)

        self.food_list = []
        self.create_food()

        self.round = 0
        self.level = 1


    def create_food(self):
        """ Set up food and initialize variables. """

        # Create food instance
        food = Food()

        # Randomly position foods
        food.x = random.randrange(20,780)
        food.y = (SCREEN_HEIGHT + 20)
        food.size = 20
        food.speed = (20)

        self.food_list.append(food)



    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH, SCREEN_HEIGHT, tile_img1)


        # Draw the current position of each food
        for food in self.food_list:
            arcade.draw_texture_rectangle(food.x, food.y, 80, 60, tile_img2)


    def update(self, delta_time):

        # Animate all the foods falling
        for food in self.food_list:
            food.y -= food.speed * delta_time
            if food.y < -20:
                food.reset_pos()
                food.speed += 5

    def on_mouse_press(self, mouse_x: float, mouse_y: float, button: int, modifiers: int):
        for food in self.food_list:
            run = mouse_x - food.x
            rise = mouse_y - food.y
            distance = math.sqrt(run*run + rise*rise)
            if distance <= 36:
                print("Clicked")
                food.reset_pos()
                food.speed += 5
            else:
                pass


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
