import arcade
from models import World, Pacman
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
class MazeWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)
 
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.pacman_sprite = ModelSprite('images/pacman.png',
                                         model=self.world.pacman)
        self.maze_drawer = MazeDrawer(self.world.maze)
 
    def update(self, delta):
        self.world.update(delta)
 
    def on_draw(self):
        arcade.start_render()
 
        self.maze_drawer.draw()                # make sure you call this before drawing pacman sprite
        self.pacman_sprite.draw()
    
    def on_key_press(self, key, key_modifiers):
         self.world.on_key_press(key, key_modifiers)

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class MazeDrawer():
    def __init__(self, maze):
        self.maze = maze
        self.width = self.maze.width
        self.height = self.maze.height
 
        self.wall_sprite = arcade.Sprite('images/wall.png')
        self.dot_sprite = arcade.Sprite('images/dot.png')
 
    def draw(self):
        for r in range(self.height):
            for c in range(self.width):
                x = c * 40 + 20
                y = r * 40 + 60
 
                if self.maze.has_wall_at(r,c):
                    self.wall_sprite.set_position(x,y)
                    self.wall_sprite.draw()
                elif self.maze.has_dot_at(r,c):
                    self.dot_sprite.set_position(x,y)
                    self.dot_sprite.draw()
 
 
def main():
    window = MazeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()