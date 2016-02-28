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
        if(((self.position.z + self.radius)  > stage.paddle0.z - 20 and (self.velocity.z > 0)) or (self.position.z -self.radius) < stage.paddle1.z + 20 and (self.velocity.z < 0)):
            self.velocity.z *= -1.1
        if(((self.position.x - self.radius) < -640 and self.velocity.x < 0) or (self.position.x + self.radius) > 640 and self.velocity.x > 0):
            self.velocity.x *= -1
        if(((self.position.y - self.radius) < -360 and self.velocity.y < 0) or (self.position.y + self.radius) > 360 and self.velocity.y > 0):
            self.velocity.y *= -1

class Stage:
    DEPTH = 2560
    def __init__(self):
        self.paddle0 = Paddle(0)
        self.paddle1 = Paddle(1)
        self.ball = Ball(Vector(0,0,500), Vector(-2, 1, 20), Vector(0,0,0), 50)

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
