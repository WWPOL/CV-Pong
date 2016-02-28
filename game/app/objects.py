from physics import Vector 

class Ball:
    def __init__(self, position, velocity, acceleration, radius):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.radius = radius
    def update(self, stage):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        if self.z == 0:
            if self.x >= paddle.x - Paddle.WIDTH / 2 and self.x <= paddle.x + Paddle.WIDTH / 2:
                if self.y >= paddle.y - Paddle.HEIGHT / 2 and self.y <= paddle.y + Paddle.HEIGHT / 2:
                    self.velocity.z *= -1
        elif self.z >= DEPTH:
            self.velocity.z *= -1

class Stage:
    DEPTH = 2560
    def __init__(self):
        self.paddle0 = Paddle(0)
        self.paddle1 = Paddle(1)
        self.ball = Ball(Vector(), Vector(x=50, y=50, z=50), Vector(), 50)

class Paddle:
    HEIGHT = 100
    WIDTH = 200
    DEPTH = 20
    def __init__(self, player_index):
        self.x = 0
        self.y = 0
        if player_index == 0:
            self.z = 0
        else:
            self.z = (-1)*Stage.DEPTH
