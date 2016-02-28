from physics import Vector 

class Ball:
    def __init__(self, position, velocity, acceleration):
        self.position = Vector()
        self.velocity = Vector()
        self.acceleration = Vector()

class Stage:
    DEPTH = 200
    def __init__(self):
        paddle0 = Paddle(0)
        paddle1 = Paddle(1)

class Paddle:
    HEIGHT = 50
    WIDTH = 50
    def __init__(self, player_index):
        self.x = 0
        self.y = 0
        if player_index == 0:
            self.z = 0
        else:
            self.z = Stage.DEPTH
