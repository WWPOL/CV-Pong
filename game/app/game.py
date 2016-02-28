import  pyglet
from pyglet.window import key
from pyglet.window import mouse

# Internal imports.
from objects import Stage
from objects import Paddle
from physics import Vector
from meta import Player
from graphics import graphics_render
from graphics import graphics_resize
from hand_detection_test import *

window = pyglet.window.Window(width=1280, height=720)
setup_camera()

def start_match():
    player1 = Player()
    player2 = Player()
    stage = Stage()

def render(self):
	graphics_render(paddle,mouseX, mouseY)
	update_hand()


@window.event
def on_draw():
    pass

@window.event
def on_resize(width, height):
    return graphics_resize(width, height)

@window.event
def on_key_press(symbol, modifier):
    if symbol == key.ESCAPE:
        pyglet.app.exit()

@window.event
def on_mouse_motion(x,y,dx,dy):
	global mouseX, mouseY
	mouseX = x - window.width/2
	mouseY = y - window.height/2


#client.establish()
#start_match()
pyglet.clock.schedule_interval(render, 1/120.0)
pyglet.app.run()

