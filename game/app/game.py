import pyglet
from pyglet.window import key

window = pyglet.window.Window(width=1280, height=720)

@window.event
def on_key_press(symbol, modifier):
    if symbol == key.ESCAPE:
        pyglet.app.exit()

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
