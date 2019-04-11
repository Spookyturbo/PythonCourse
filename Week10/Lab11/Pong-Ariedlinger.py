#Pong
#Andrew Riedlinger
#April 11th, 2019
#
#A 1 player game of pong with 3 walls

from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Paddle(games.Sprite):
    """The player controlled paddle for reflecting the ball"""
    image = games.load_image("paddle.png")

    def __init__(self):
        super().__init__(image = Paddle.image,
                         x = 20, y = games.mouse.y)

        self.score = games.Text(value = 0, size = 25, color = color.white,
                                top = 20, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        self.y = games.mouse.y

        if self.bottom > games.screen.height:
            self.bottom = games.screen.height

        if self.top < 0:
            self.top = 0

        self.check_collide()

    def check_collide(self):
        """Checks for collisions with balls"""
        for ball in self.overlapping_sprites:
            ball.handle_collide()
            self.score.value += 10
            self.score.right = games.screen.width - 10

class Ball(games.Sprite):
    """The ball to play pong with"""
    image = games.load_image("ball.png")
    x_speed = 2
    y_speed = 2
    def __init__(self):
        super().__init__(image = Ball.image,
                         x = games.screen.width / 2,
                         y = games.screen.height / 2,
                         dy = -1 * Ball.y_speed,
                         dx = -1 * Ball.x_speed)

    def update(self):
        """Determine if needs to bounce of walls"""
        if self.top < 0 or self.bottom > games.screen.height:
            self.dy = -self.dy

        if self.right > games.screen.width:
            self.dx = -self.dx

        if self.left < 0:
            self.end_game()

    def handle_collide(self):
        self.dx = -self.dx

    def end_game(self):
        """End the game"""
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width / 2,
                                    y = games.screen.height / 2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

def main():
    background = games.load_image("background.png", transparent = False)
    games.screen.background = background

    paddle = Paddle()
    games.screen.add(paddle)

    ball = Ball()
    games.screen.add(ball)

    games.mouse.is_visible = False
    games.screen.event_grab = True
    
    games.screen.mainloop()

main()
