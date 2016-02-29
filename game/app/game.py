#!/usr/bin/env python2.7 
import pyglet
from pyglet.window import key
from pyglet.window import mouse
import thread

# Internal imports.
from objects import Stage
from objects import Paddle
from physics import Vector
from graphics import graphics_render
from graphics import graphics_resize
from graphics import on_window_create
from hand import HandJob

window = pyglet.window.Window(width=1280, height=720)
on_window_create()
hand = HandJob()
stage = Stage()

def render(self):
    graphics_render(hand, stage)
    stage.ball.update(stage)

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

pyglet.clock.schedule_interval(render, 1/30.0)
pyglet.app.run()
