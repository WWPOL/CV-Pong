import pyglet
from pyglet.gl import *
from pyglet.window import key
from objects import Ball
from physics import Vector
from graphics import drawCircle

window = pyglet.window.Window(width=1280, height=720)

ball = Ball(Vector(), Vector(), Vector())

@window.event
def on_key_press(symbol, modifier):
    if symbol == key.ESCAPE:
        pyglet.app.exit()

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0,0,-5)
    drawCircle(0,0,0,1,30)
    drawCircle(4,0,-3,1,30)

@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65, width / float(height), .1, 1000)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

pyglet.app.run()
