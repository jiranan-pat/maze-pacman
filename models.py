import arcade.key

MOVEMENT_SPEED = 2.5

DIR_STILL = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
 
DIR_OFFSETS = { DIR_STILL: (0,0),
                DIR_UP: (0,1),
                DIR_RIGHT: (1,0),
                DIR_DOWN: (0,-1),
                DIR_LEFT: (-1,0) }

class Pacman:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
 
        self.direction = DIR_STILL
 
    def move(self, direction):
        self.x += MOVEMENT_SPEED * DIR_OFFSETS[direction][0]
        self.y += MOVEMENT_SPEED * DIR_OFFSETS[direction][1]
 
    def update(self, delta):
        self.move(self.direction)
 
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.pacman = Pacman(self, width // 2, height // 2)
        self.maze = Maze(self)
 
    def update(self, delta):
        self.pacman.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.pacman.direction = DIR_UP
        if key == arcade.key.DOWN:
            self.pacman.direction = DIR_DOWN
        if key == arcade.key.LEFT:
            self.pacman.direction = DIR_LEFT
        if key == arcade.key.RIGHT:
            self.pacman.direction = DIR_RIGHT
    

class Maze:
    def __init__(self, world):
        self.map = [ '####################',
                     '#..................#',
                     '#.###.###..###.###.#',
                     '#.#...#......#...#.#',
                     '#.#.###.####.###.#.#',
                     '#.#.#..........#.#.#',
                     '#.....###..###.....#',
                     '#.#.#..........#.#.#',
                     '#.#.###.####.###.#.#',
                     '#.#...#......#...#.#',
                     '#.###.###..###.###.#',
                     '#..................#',
                     '####################' ]
        self.height = len(self.map)
        self.width = len(self.map[0])
    
    def has_wall_at(self, r, c):
        return self.map[r][c] == '#'
 
    def has_dot_at(self, r, c):
        return self.map[r][c] == '.'