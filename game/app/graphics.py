import math
import pyglet
from pyglet.gl import *
from objects import Ball
from objects import Paddle
from physics import Vector

def draw_circle(ball):
    num_segments = 30
    angle = 2 * math.pi / float(num_segments)
    tan = math.tan(angle)
    radial = math.cos(angle)
    x = ball.radius
    y = 0
    glColor3f(255,0,0)
    glBegin(GL_POLYGON)
    for i in range(0, num_segments):
        glVertex3d(x + ball.position.x, y + ball.position.y, ball.position.z)
        tx = -y
        ty = x
        x+=tx*tan
        y+=ty*tan
        x*=radial
        y*=radial
    glEnd()
    glColor3f(255,255,255)
    x = ball.radius
    y = 0
    glBegin(GL_POLYGON)
    for i in range(0, num_segments):
        glVertex3d(x + ball.position.x, -360, ball.position.z + y)
        tx = -y
        ty = x
        x+=tx*tan
        y+=ty*tan
        x*=radial
        y*=radial
    glEnd()

def draw_paddle(paddle):
    z = 0;
    if(paddle.z == 0):
        z = (paddle.z - paddle.DEPTH/2)
    else:
        z = (paddle.z + paddle.DEPTH/2)

    glBegin(GL_QUADS)
    #FRONT
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    #BACK
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z - (paddle.DEPTH/2)) 
    #LEFT
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    #RIGHT
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    #UP
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    #DOWN
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glEnd()

    glColor3f(0,255,0)

    glBegin(GL_LINE_LOOP)
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z - (paddle.DEPTH/2)) 
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glEnd()  

    glBegin(GL_LINES)
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glEnd()

    glBegin(GL_LINES)
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x + (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glEnd()

    glBegin(GL_LINES)
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y + (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glEnd()

    glBegin(GL_LINES)
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z + (paddle.DEPTH/2))
    glVertex3d(paddle.x - (paddle.WIDTH/2), paddle.y - (paddle.HEIGHT/2), z - (paddle.DEPTH/2))
    glEnd()  

    glColor3f(255,255,255)



def draw_stage():
    glBegin(GL_LINE_LOOP)
    glVertex3d(-640,360,-2560)
    glVertex3d(640,360,-2560)
    glVertex3d(640,-360,-2560)
    glVertex3d(-640,-360,-2560)
    glEnd()
    glBegin(GL_LINES)
    glVertex3d(-640,360,0)
    glVertex3d(-640,360,-2560)
    glEnd()
    glBegin(GL_LINES)
    glVertex3d(640,360,0)
    glVertex3d(640,360,-2560)
    glEnd()
    glBegin(GL_LINES)
    glVertex3d(640,-360,-2560)
    glVertex3d(640,-360,0)
    glEnd()
    glBegin(GL_LINES)
    glVertex3d(-640,-360,0)
    glVertex3d(-640,-360,-2560)
    glEnd()

def graphics_render(hand, stage):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0,0,-565)

    position, velocity = hand.captureImage()
    stage.paddle0.x = (position[0] * 2) - 640
    stage.paddle0.y = 360 - int(position[1] * 1.5)
    stage.paddle0.vx = velocity[0]
    stage.paddle0.vy = velocity[1]
    stage.paddle1.x = stage.ball.position.x
    stage.paddle1.y = stage.ball.position.y
    draw_stage()
    
    draw_paddle(stage.paddle1)

    draw_circle(stage.ball)

    draw_paddle(stage.paddle0)

def graphics_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65, width / float(height), .1, 100000000)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED



