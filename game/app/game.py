import pyglet
from pyglet.window import key

# Internal imports.
from objects import Stage 
from physics import Vector
from meta import Player 

window = pyglet.window.Window(width=1280, height=720)

def start_match():
    player1 = Player()
    player2 = Player()
    stage = Stage()

@window.event
def on_key_press(symbol, modifier):
    if symbol == key.ESCAPE:
        pyglet.app.exit()

@window.event
def on_draw():
    window.clear()

start_match()
pyglet.app.run()
