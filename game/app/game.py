import  pyglet
from pyglet.window import key

# Internal imports.
from objects import Stage
from physics import Vector
from meta import Player
from graphics import graphics_render

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
    grahpics_render()

@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65, width / float(height), .1, 1000)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

start_match()
pyglet.app.run()
