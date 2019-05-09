#Space Invaders
#Andrew Riedlinger
#May 1st, 2019
#
#A space invader inspired game

#the die method is not in one wrapper class because I use a mixture
#of sprites and Animations, and having more then one wrapper class for the same purpose
#would just be more confusing

from superwires import games, color
import random
import math

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Bug(games.Animation):
    """A enemy to the player"""
    image_files = ["./Images/fly1.bmp", "./Images/fly2.bmp"]

    POINTS = 10
    total = 0

    FIRE_CHANCE = 1 / 100
    MISSILE_BUFFER = 20
    #This delay is only necessary so the Bug doesn't fire twice so fast it shoots its own missile.
    MISSILE_DELAY = 10
    
    def __init__(self, game, x, y):
        super().__init__(images = Bug.image_files,
                         x = x,
                         y = y,
                         repeat_interval = 25)
        self.game = game
        games.screen.add(self)
        Bug.total += 1
        self.missile_wait = 0

    def update(self):
        """Manages the bug firing back"""
        if self.missile_wait > 0:
            self.missile_wait -= 1
            
        fire_missile = random.random()
        if fire_missile <= Bug.FIRE_CHANCE and self.missile_wait == 0:
            Missile(self.x, self.y + Bug.MISSILE_BUFFER, 1, source = "Bug")
            self.missile_wait = Bug.MISSILE_DELAY

    def die(self, killer):
        """Destroys this object, returns true if successful"""
        if killer == "Bug":
            return False
        
        Bug.total -= 1
        self.game.score.value += int(Bug.POINTS)
        self.game.score.right = games.screen.width - 10

        if Bug.total == 0:
            self.game.advance()
        
        self.destroy()
        return True
        
class Ship(games.Sprite):
    """The players ship"""
    image = games.load_image("./Images/ship.bmp")

    MISSILE_DELAY = 25
    MISSILE_BUFFER = -20
    
    SPEED = 5
    
    SPAWN_Y = games.screen.height - 20
    EDGE_BUFFER = 5

    def __init__(self, game, x):
        super().__init__(image = Ship.image, x = x, y = Ship.SPAWN_Y)
        self.missile_wait = 0
        self.game = game

    def update(self):
        #Control left and right movement
        if games.keyboard.is_pressed(games.K_LEFT):
            self.dx = -Ship.SPEED  
        elif games.keyboard.is_pressed(games.K_RIGHT):
            self.dx = Ship.SPEED
        else:
            self.dx = 0

        #Keep ship on screen
        if self.left < Ship.EDGE_BUFFER:
            self.left = Ship.EDGE_BUFFER

        if self.right > games.screen.width - Ship.EDGE_BUFFER:
            self.right = games.screen.width - Ship.EDGE_BUFFER

        #Fire missiles
        if self.missile_wait > 0:
            self.missile_wait -= 1
            
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            Missile(self.x, self.y + Ship.MISSILE_BUFFER, -1)
            self.missile_wait = Ship.MISSILE_DELAY
        
    def die(self, killer):
        """Destroys this object, returns true if successful"""
        if killer == "Ship":
            return False
        self.destroy()
        self.game.end()
        return True
    
class Missile(games.Sprite):
    """Missile launched by players and bugs alike"""
    image = games.load_image("./Images/missile.bmp")
    sound = games.load_sound("./Sounds/missile.wav")

    VELOCITY_FACTOR = 10
    LIFETIME = 100

    def __init__(self, x, y, dy, source = "Ship"):
        """Create Missile (dy -1 or 1, used for up or down)"""
        Missile.sound.play()

        #Ensures is either -1 or 1
        if dy != 0:
            dy = dy / abs(dy)
        
        #Create the missile
        super().__init__(image = Missile.image,
                         x = x, y = y,
                         dx = 0, dy = dy * Missile.VELOCITY_FACTOR)

        self.lifetime = Missile.LIFETIME
        self.source = source
        games.screen.add(self)

    def update(self):
        """Move the missile"""
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()
    
        #Kill what gets shot
        if self.overlapping_sprites:
            #Used to rule out falsely shooting self or bugs shooting other bugs
            successful = False
            for sprite in self.overlapping_sprites:
                if sprite.die(self.source):
                    successful = True
            if successful:
                Explosion(self.x, self.y)
                self.die(self.source)
        
    def die(self, killer):
        """Destroys this object, returns true if successful"""
        self.destroy()
        return True
    
    

class Explosion(games.Animation):
    """Explosion Animation."""
    sound = games.load_sound("./Sounds/explosion.wav")
    images = ["./Images/explosion1.bmp",
              "./Images/explosion2.bmp",
              "./Images/explosion3.bmp",
              "./Images/explosion4.bmp",
              "./Images/explosion5.bmp",
              "./Images/explosion6.bmp",
              "./Images/explosion7.bmp",
              "./Images/explosion8.bmp",
              "./Images/explosion9.bmp"]

    def __init__(self, x, y):
        super().__init__(images = Explosion.images,
                         x = x, y = y,
                         repeat_interval = 4, n_repeats = 1,
                         is_collideable = False)

        Explosion.sound.play()
        games.screen.add(self)

class Game(object):
    """The game"""

    MAX_BUGS_PER_ROW = 8
    BUGS_PER_LEVEL = 2
    DISTANCE_BETWEEN_ROWS = 40
    
    def __init__(self):
        self.level = 0
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)

        self.ship = Ship(game = self, x = games.screen.width / 2)
        games.screen.add(self.ship)

    def play(self):
        """Play the game!"""
        games.music.load("./Sounds/theme.mid")
        games.music.play(-1)

        background_image = games.load_image("./Images/Background.jpg")
        games.screen.background = background_image

        self.advance()

        games.screen.mainloop()

    def advance(self):
        self.level += 1

        #Spawn Bugs
        number_bugs = self.level * Game.BUGS_PER_LEVEL

        #Set edge buffer and default space between bugs when a row is full
        edge_buffer = 10
        bug_buffer = (games.screen.width - 2 * edge_buffer) / Game.MAX_BUGS_PER_ROW

        rows = number_bugs / Game.MAX_BUGS_PER_ROW

        #If more then 8 bugs, a new row is needed
        if rows % 1 > 0:
            rows = (rows + 1 - (rows % 1))
        rows = int(rows)
        
        for row in range(rows):
            #if on last row and it isn't full calculate new bugs_in_row
            if row == rows-1:
                bugs_in_row = Game.MAX_BUGS_PER_ROW if number_bugs % Game.MAX_BUGS_PER_ROW == 0 else number_bugs % Game.MAX_BUGS_PER_ROW
            else:
                bugs_in_row = Game.MAX_BUGS_PER_ROW
                
            bug_buffer = (games.screen.width - 2 * edge_buffer) / (bugs_in_row + 1)
                
            for i in range(1, bugs_in_row + 1):
                Bug(game = self, x = i * bug_buffer, y = 20 + row * Game.DISTANCE_BETWEEN_ROWS)

        level_message = games.Message(value = "Level " + str(self.level),
                                      size = 40,
                                      color = color.yellow,
                                      x = games.screen.width / 2,
                                      y = games.screen.height / 2,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

    def end(self):
        """End the game"""
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width / 2,
                                    y = games.screen.height / 2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)
        

def main():
    space_invaders = Game()
    space_invaders.play()

main()
