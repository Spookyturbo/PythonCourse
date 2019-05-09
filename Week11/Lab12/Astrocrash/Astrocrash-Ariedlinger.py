#Astrocrash
#Andrew Riedlinger
#April 25th, 2019
#
#The popular game asteroids remade

from superwires import games, color
import random
import math

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Wrapper(games.Sprite):
    """A sprite that wraps around the screen."""

    def update(self):
        """Wrap sprite around screen"""
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """Destroy Self"""
        self.destroy()

class Collider(Wrapper):
    """A Wrapper that can collide with another object"""
    def update(self):
        super().update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

class Asteroid(Wrapper):
    """An asteroid which floats across the screen."""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("./Images/asteroid_small.bmp"),
              MEDIUM : games.load_image("./Images/asteroid_med.bmp"),
              LARGE : games.load_image("./Images/asteroid_big.bmp") }

    SPEED = 2
    SPAWN = 2

    POINTS = 30
    total = 0

    def __init__(self, game, x, y, size):
        """Initialize asteroid sprite"""
        super().__init__(image = Asteroid.images[size],
                         x = x, y = y,
                         dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                         dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)

        self.size = size
        self.game = game
        Asteroid.total += 1


    def die(self):
        """Destroy asteroid"""
        #If asteroid isnt smalle, replace with two smaller asteroids
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game = self.game,
                                        x = self.x,
                                        y = self.y,
                                        size = self.size - 1)
                games.screen.add(new_asteroid)

        super().die()
        
        Asteroid.total -= 1
        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10

        if Asteroid.total == 0:
            self.game.advance()
        


class Ship(Collider):
    """The players ship"""
    image = games.load_image("./Images/ship.bmp")
    sound = games.load_sound("./Sound/thrust.wav")
    
    ROTATION_STEP = 3
    VELOCITY_STEP = 0.03
    MISSILE_DELAY = 25
    VELOCITY_MAX = 3

    def __init__(self, game, x, y):
        super().__init__(image = Ship.image, x = x, y = y)
        self.game = game
        self.missile_wait = 0

    def update(self):
        """Movement and Control"""
        super().update()
        
        #Rotation
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP

        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP

        #Move Forward
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()

            angle = self.angle * math.pi / 180 #Convert to radians

            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)

        if self.missile_wait > 0:
            self.missile_wait -= 1

        #Fire missile
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

    def die(self):
        """Destroy ship and end game"""
        self.game.end()
        super().die()

class Missile(Collider):
    """A missile launched by the player"""
    image = games.load_image("./Images/missile.bmp")
    sound = games.load_sound("./Sound/missile.wav")

    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        """Initialize missle sprite"""
        Missile.sound.play()
        #convert to radians
        angle = ship_angle * math.pi / 180

        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        #create the missile
        super().__init__(image = Missile.image,
                         x = x, y = y,
                         dx = dx, dy = dy)

        self.lifetime = Missile.LIFETIME

    def update(self):
        """Move the missile"""
        super().update()
        #if lifetime up, destroy missile
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()
            

class Explosion(games.Animation):
    """Explosion Animation."""
    sound = games.load_sound("./Sound/explosion.wav")
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

class Game(object):
    """ The game itself """
    def __init__(self):
        """Initialize the game"""
        self.level = 0
        self.sound = games.load_sound("./Sound/level.wav")
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)

        games.screen.add(self.score)

        self.ship = Ship(game = self,
                         x = games.screen.width / 2,
                         y = games.screen.height / 2)

        games.screen.add(self.ship)

    def play(self):
        """Play the game"""
        games.music.load("./Sound/theme.mid")
        games.music.play(-1)

        nebula_image = games.load_image("./Images/nebula.jpg")
        games.screen.background = nebula_image

        #Go to next level
        self.advance()

        games.screen.mainloop()

    def advance(self):
        """Advance to next level"""
        self.level += 1

        BUFFER = 150

        #create new asteroids
        for i in range(self.level):
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            x = self.ship.x + x_distance
            y = self.ship.y + y_distance

            #Wrap around screen if necessary
            x %= games.screen.width
            y %= games.screen.height

            new_asteroid = Asteroid(game = self,
                                    x = x, y = y,
                                    size = Asteroid.LARGE)
            games.screen.add(new_asteroid)

        #display level number
        level_message = games.Message(value = "Level " + str(self.level),
                                      size = 40,
                                      color = color.yellow,
                                      x = games.screen.width / 2,
                                      y = games.screen.width / 10, #This doesnt seem right
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

        #play new level sound
        if self.level > 1:
            self.sound.play()

    def end(self):
        """End the game"""
        #Show gameover for 5 seconds
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
    astrocrash = Game()
    astrocrash.play()

main()





        

