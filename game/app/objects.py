from physics import Vector 

class Ball:
    RADIUS = 10
    def __init__(self, position, velocity, acceleration):
        self.position = Vector()
        self.velocity = Vector()
        self.acceleration = Vector()

class Paddle:
    def __init__(self, player):
        if player = 0:
            self.z = 0
        else:
            self.z = Stage.DEPTH

class Stage:
    DEPTH = 200

    def __init__(self):
        self.ball = Ball(Vector(), Vector(), Vector())
        self.player0 = Paddle(0)
        self.player1 = Paddle(1)
