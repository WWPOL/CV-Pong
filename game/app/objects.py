from physics import Vector 

class Ball:
    def __init__(self, position, velocity, acceleration, radius):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.radius = radius

class Stage:
    DEPTH = 2560
    def __init__(self):
        paddle0 = Paddle(0)
        paddle1 = Paddle(1)

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
