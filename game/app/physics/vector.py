class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.y
