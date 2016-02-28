import pyglet
from pyglet.window import key
from ball import Ball
from physics import Vector

window = pyglet.window.Window(width=1280, height=720)

ball = Ball(Vector(), Vector(), Vector())

@window.event
def on_key_press(symbol, modifier):
    if symbol == key.ESCAPE:
        pyglet.app.exit()

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
